from django.contrib import admin
from django.contrib import admin
from .models import ExcerciseCategory, Excercise, Person, Measurement, News, ExcerciseMuscles, Module, ModuleExercise, TrainingModule, TrainingPlan


# Register your models here.

@admin.register(ExcerciseCategory)
class ExcerciseCategoryAdmin(admin.ModelAdmin):
    list_display = ('CategoryName',)  # Wyświetlana kolumna w liście obiektów w panelu admina

@admin.register(ExcerciseMuscles)
class ExcerciseMusclesAdmin(admin.ModelAdmin):
    list_display = ('MuscleName',)  # Wyświetlana kolumna w liście obiektów w panelu admina

@admin.register(Excercise)
class ExcerciseAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Category', 'Description', 'ExcerciseLinkUrl')  # Wyświetlana kolumna w liście obiektów w panelu admina
    list_filter = ('Category',)  # Filtrowanie po kategorii

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['FirstName','SecondName', 'PhoneNumber', 'Email']
    search_fields = ['FirstName']

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['Date', 'Person', 'Weight', 'Growth', 'BFR', 'BodyWater', 'Chest', 'LeftArm', 'RightArm' ]
    
    
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['NewsText', 'NewsDate']

class ModuleExerciseInline(admin.TabularInline):
    model = ModuleExercise
    extra = 1  # Pozwala na dodawanie jednego lub więcej powiązań ModuleExercisey
    
    def has_change_permission(self, request, obj=None):
        return False
    
@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['Description', 'Type']
    inlines = [ModuleExerciseInline]

class TrainingModuleInline(admin.TabularInline):
    model = TrainingModule
    extra = 1  # Pozwala na dodawanie jednego lub więcej powiązań ModuleExercisey   
    
@admin.register(TrainingPlan)
class TrainingPlanAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Type']
    inlines = [TrainingModuleInline]
    
