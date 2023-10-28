# views.py

from django.shortcuts import render, redirect
from .models import Person, Excercise, ExcerciseCategory, News, ExcerciseMuscles, Module, ModuleExercise
from .forms import PersonForm, ExcerciseForm, ModuleExerciseForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView

def person_list(request):
    people = Person.objects.filter(Photo__isnull=False)  # Pobierz tylko rekordy z przypisanym plikiem Photo
    context = {'people': people}
    return render(request, 'person_list.html', context)


def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request, 'add_person.html', {'form': form})

def excercise_list(request):
    categories = ExcerciseCategory.objects.all()  # Pobierz dostępne kategorie
    excercises = Excercise.objects.all()  # Pobierz wszystkie ćwiczenia

    # Rozszerz obiekty ćwiczeń o atrybut muscle_names
    for excercise in excercises:
        muscles = excercise.DirectMus.all()
        excercise.muscle_names = ", ".join([muscle.MuscleName for muscle in muscles])

    context = {'excercises': excercises, 'categories': categories}
    return render(request, 'excercise.html', context)


def add_excercise(request):
    if request.method == 'POST':
        form = ExcerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('excercise_list')  # Przekierowanie do listy ćwiczeń po dodaniu ćwiczenia
    else:
        form = ExcerciseForm()
    return render(request, 'add_excercise.html', {'form': form})

def edit_excercise(request, excercise_id):
    excercise = Excercise.objects.get(id=excercise_id)

    if request.method == 'POST':
        form = ExcerciseForm(request.POST, instance=excercise)
        if form.is_valid():
            form.save()
            return redirect('excercise_list')
    else:
        form = ExcerciseForm(instance=excercise)

    muscles = excercise.DirectMus.all()
    muscle_names = ", ".join([muscle.MuscleName for muscle in muscles])

    context = {
        'form': form,
        'excercise': excercise,
        'muscle_names': muscle_names,
    }

    return render(request, 'edit_excercise.html', context)


def home(request):
    return render(request, 'home.html')

def temp(request):
    return render(request, 'temp.html')

def startingpage2(request):
    return render(request, 'startingpage2.html')


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news_items = News.objects.all()
        context['news_items'] = news_items
        return context


def login_page(request):
    # Pobierz dane z modelu News
    news_items = News.objects.all()

    return render(request, 'login.html', {'news_items': news_items})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Przekierowanie po udanej rejestracji
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


def person(request, person_id):
    
    person = Person.objects.get(id=person_id)

    context = {
        'person': person,
    }

    return render(request, 'person.html', context)

def add_module_exercise(request, module_id):
    if request.method == 'POST':
        form = ModuleExerciseForm(request.POST)
        if form.is_valid():
            module_exercise = form.save(commit=False)
            module_exercise.module_id = module_id
            module_exercise.save()
            return redirect('nazwa_widoku_detalu_modulu', module_id=module_id)
    else:
        form = ModuleExerciseForm()

    return render(request, 'add_exc.html', {'form': form})

class ModuleListView(ListView):
    model = Module
    template_name = 'module_list.html'
    context_object_name = 'modules'

def module_detail(request, module_id):
    module = Module.objects.get(pk=module_id)
    exercises = ModuleExercise.objects.filter(Module=module)  # Filtruj ćwiczenia przypisane do danego modułu
    
    if request.method == 'POST':
        form = ModuleExerciseForm(request.POST)
        if form.is_valid():
            module_exercise = form.save(commit=False)
            module_exercise.Module = module  # Przypisanie aktualnego modułu
            module_exercise.save()
            return redirect('module_detail', module_id=module_id)
    else:
        form = ModuleExerciseForm()

    return render(request, 'module_detail.html', {'module': module, 'exercises': exercises, 'form': form})



