from django.db import models

Excercise_TYPE = (
    ('maszyna', 'Maszyna'),
    ('wolne','Wolny ciężar'),
    ('wymienne','Wymienne'),
    ('inny','Inny')
)
Module_TYPE = (
    ('cardio', 'Cardio'),
    ('mobility','Mobility'),
    ('siłowy','Siłowy'),
    ('fbw','FBW')
)

# Modele związane z TrenerApp

class ExcerciseCategory(models.Model):
    CategoryName = models.CharField(max_length=255, verbose_name='Kategoria')


    def __str__(self):
        return self.CategoryName
    
    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

class ExcerciseMuscles(models.Model):
    MuscleName = models.CharField(max_length=255, verbose_name='Grupa mięśni')


    def __str__(self):
        return self.MuscleName
        
    class Meta:
        verbose_name = "Grupa mięśni"
        verbose_name_plural = "Grupy mięśni"

class Excercise(models.Model):
    Name = models.CharField(max_length=300, verbose_name='Nazwa ćwiczenia')
    Category = models.ForeignKey(ExcerciseCategory, verbose_name='Kategoria', on_delete=models.CASCADE)
    DirectMus = models.ManyToManyField(ExcerciseMuscles, verbose_name='Grupy mięśni')
    Description = models.TextField(verbose_name='Opis ćwiczenia')
    Type = models.CharField(choices=Excercise_TYPE, verbose_name='Typ ćwiczenia', max_length=30, default='inny')
    ExcerciseLinkUrl = models.URLField(verbose_name ='Link do filmu', null=True, blank=True)
    NameEng = models.CharField(max_length=150, verbose_name='Nazwa ćwiczenia (ENG)', null=True, blank=True)
    ImageFront = models.ImageField(verbose_name= "Zdjęcie przednie aktony", null=True, blank=True)
    ImageSide = models.ImageField(verbose_name= "Zdjęcie boczne aktony", null=True, blank=True)
    ImageBack = models.ImageField(verbose_name= "Zdjęcie tylne aktony", null=True, blank=True)
    
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Ćwiczenie"
        verbose_name_plural = "Ćwiczenia"
        
class Person(models.Model):
    FirstName = models.CharField(max_length=255, verbose_name='Imię')
    SecondName = models.CharField(max_length=255, verbose_name='Nazwisko')
    Email = models.CharField(max_length=255, verbose_name='e-mail')
    PhoneNumber = models.CharField(max_length=255, verbose_name='Numer telefonu')
    Photo = models.ImageField(upload_to='images/', null=True, blank=True)
    
        
    def __str__(self):
        return self.FirstName
    
    class Meta:
        verbose_name = "Osoba"
        verbose_name_plural = "Osoby"

class Measurement(models.Model):
    Date = models.DateField(verbose_name='Data pomiaru')
    Person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Osoba')
    Weight = models.DecimalField(decimal_places=2,max_digits=5, verbose_name='Waga w kg', null=True, blank=True)
    Growth = models.DecimalField(decimal_places=0, max_digits=5, verbose_name='Wzrost w cm', null=True, blank=True)
    BFR = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Poziom tkanki tłuszczowej w %', null=True, blank=True)
    BodyWater = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Poziom wody w organiźmie w %', null=True, blank=True)
    Chest = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Klatka piersiowa cm', null=True, blank=True)
    LeftArm = models.DecimalField(decimal_places=2, max_digits=5, verbose_name=' Lewe ramię w cm', null=True, blank=True)
    RightArm = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Prawe ramię w cm', null=True, blank=True)
    Abdomen = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Obwód brzucha w cm', null=True, blank=True)
    Waist = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Talia w cm', null=True, blank=True)
    Hips = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Biodra w cm', null=True, blank=True)
    LeftThigh = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Lewe udo w cm', null=True, blank=True)
    RightThigh = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Prawe udo w cm', null=True, blank=True)
    Desc = models.TextField(verbose_name='Opis', null=True, blank=True)
    
    def __str__(self):
        return self.Desc
    
    class Meta:
        verbose_name = "Pomiar"
        verbose_name_plural = "Pomiary"     
        
class News(models.Model):
    NewsText = models.CharField(max_length=255, verbose_name='News')
    NewsDate = models.DateField()    
        
    def __str__(self):
        return self.NewsText
    
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        
        
class Module(models.Model):
    Description = models.CharField(max_length=200, verbose_name= 'Nazwa modułu', null=True, blank=True)
    Type = models.CharField(choices=Module_TYPE, verbose_name='Typ modułu', max_length=30, default='Mobility')
    FullDescription = models.TextField(verbose_name= 'Opis modułu', null=True, blank=True)
    Exercises = models.ManyToManyField(Excercise, through='ModuleExercise')
    
    def __str__(self):
        return self.Description
    
    class Meta:
        verbose_name = "Moduł"
        verbose_name_plural = "Moduły"     

class ModuleExercise(models.Model):
    Module = models.ForeignKey(Module, on_delete=models.CASCADE)
    Exercise = models.ForeignKey(Excercise, on_delete=models.CASCADE)
    Series = models.PositiveIntegerField (verbose_name='Ilość serii', default=0)
    Repetitions = models.PositiveIntegerField(verbose_name='Ilość powtórzeń w serii', default=0)
    Weight = models.PositiveIntegerField(verbose_name='Ciężar na powtórzenie', default=0)
    Duration = models.PositiveIntegerField(verbose_name='Czas trwania ćwiczenia (jeśli dotyczy)', default=0)
    
    def __str__(self):
        return f"{self.Module} - {self.Exercise}"

    class Meta:
        verbose_name = "Połączenie Moduł-Ćwiczenie"
        verbose_name_plural = "Połączenia Moduł-Ćwiczenie"

class TrainingPlan(models.Model):
    Name = models.CharField(max_length=200, verbose_name= 'Nazwa treningu', null=True, blank=True)
    Type = models.CharField(choices=Module_TYPE, verbose_name='Typ treningu', max_length=30, default='Mobility')
    FullDescription = models.TextField(verbose_name= 'Opis treningu', null=True, blank=True)
    Module = models.ManyToManyField(Module, through='TrainingModule')
    
    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name = "Plan treningowy"
        verbose_name_plural = "Plany treningowe"     
        
class TrainingModule(models.Model):
    Training = models.ForeignKey(TrainingPlan, on_delete=models.CASCADE)
    Module = models.ForeignKey(Module, on_delete=models.CASCADE)
        
    def __str__(self):
        return f"{self.Training} - {self.Module}"

    class Meta:
        verbose_name = "Połączenie Plan-moduł"
        verbose_name_plural = "Połączenia Plan-moduł"