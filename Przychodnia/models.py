from django.db import models
from django.contrib.auth.models import User

class Pacjenci(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    id_pacjenta = models.PositiveIntegerField(primary_key=True)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)
    miejscowo = models.CharField(max_length=20)
    kod_pocztowy = models.CharField(max_length=6)
    numer_telefonu = models.IntegerField()
    PESEL = models.CharField(max_length=11)

class Lekarze(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    id_lekarze = models.PositiveIntegerField (primary_key=True)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)
    miejscowo = models.CharField(max_length=20)
    kod_pocztowy = models.CharField(max_length=6)
    numer_telefonu = models.IntegerField()
    Wyksztalcenie = models.CharField(max_length=20)
    Specjalizacja = models.CharField(max_length=20)
    PESEL = models.CharField(max_length=11)

class Wizyty(models.Model):
    id_wizyty = models.PositiveIntegerField(primary_key=True)
    id_lekarze = models.ForeignKey(Lekarze,on_delete=models.CASCADE)
    id_pacjenta = models.ForeignKey(Pacjenci,on_delete=models.CASCADE)
    data_wizyty = models.DateField()
    godzina_wizyty = models.TimeField()
    Opis = models.CharField(max_length=20)
    numer_recepty = models.IntegerField()
    numer_skierowania = models.IntegerField()
