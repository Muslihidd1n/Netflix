from django.db import models
from django.contrib.auth.models import User

class Aktyor(models.Model):
    ism = models.CharField(max_length=20)
    tugilgan_sana = models.DateField(blank=True)
    jins = models.CharField(max_length=20)
    davlat = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.ism


class Kino(models.Model):
    nom = models.CharField(max_length=30)
    janr = models.CharField(max_length=30)
    yil = models.DateField(blank=True)
    aktyorlar = models.ManyToManyField(Aktyor)

    def __str__(self):
        return self.nom

class Tarif(models.Model):
    nom = models.CharField(max_length=30)
    davomiylik = models.PositiveIntegerField(blank=True, null=True)
    narx = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.nom

class KinoAktyor(models.Model):
    kino = models.ForeignKey(Kino, on_delete=models.CASCADE)
    aktyor = models.ForeignKey(Aktyor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.kino.nom}: {self.aktyor}"


class Izoh(models.Model):
    matn = models.CharField(max_length=300)
    sana = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kino = models.ForeignKey(Kino, on_delete=models.CASCADE)
    baho = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.matn



