from django import forms
from .models import Person, Excercise, ExcerciseMuscles, ModuleExercise

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('FirstName', 'SecondName', 'Email', 'PhoneNumber', 'Photo')


class ExcerciseForm(forms.ModelForm):
    # Tworzymy pole ModelMultipleChoiceField dla grup mięśni
    DirectMus = forms.ModelMultipleChoiceField(
        queryset=ExcerciseMuscles.objects.all(),  # Pobieramy dostępne grupy mięśni
        widget=forms.CheckboxSelectMultiple,  # Używamy widżetu z checkboxami
        required=False,  # Ustawiamy na nieobowiązkowe, jeśli potrzebujesz
    )

    class Meta:
        model = Excercise
        fields = ('Name', 'DirectMus', 'Category', 'Description', 'Type', 'ExcerciseLinkUrl', 'NameEng')

class ModuleExerciseForm(forms.ModelForm):
    class Meta:
        model = ModuleExercise
        fields = ['Exercise', 'Series', 'Repetitions', 'Weight', 'Duration']