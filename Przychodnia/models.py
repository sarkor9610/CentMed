from django.db import models

class Pacjenci(models.Model):
    id_pacjenta = models.IntegerField(primary_key=True)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)
    miejscowo = models.CharField(max_length=20)
    kod_pocztowy = models.CharField(max_length=6)
    numer_telefonu = models.CharField(max_length=9)
    PESEL = models.CharField(max_length=11)

class Lekarze(models.Model):
    id_lekarze = models.IntegerField(primary_key=True)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)
    miejscowo = models.CharField(max_length=20)
    kod_pocztowy = models.CharField(max_length=6)
    numer_telefonu = models.CharField(max_length=6)
    Wyksztalcenie = models.CharField(max_length=20)
    Specjalizacja = models.CharField(max_length=20)
    PESEL = models.CharField(max_length=11)

class Wizyty(models.Model):
    id_wizyty = models.IntegerField(primary_key=True)
    id_lekarze = models.ForeignKey(Lekarze,on_delete=models.CASCADE)
    id_pacjenta = models.ForeignKey(Pacjenci,on_delete=models.CASCADE)
    data_wizyty = models.DateField()
    godzina_wizyty = models.DateField()
    Opis = models.CharField(max_length=20)
    numer_recepty = models.IntegerField(max_length=20)
    numer_skierowania = models.IntegerField(max_length=20)
