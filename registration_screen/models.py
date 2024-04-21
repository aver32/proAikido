from django.contrib.auth.hashers import make_password
from django.db import models


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("ФИО", default="", max_length=255)
    email = models.CharField(verbose_name="Email", max_length=255, default="")
    password = models.CharField(max_length=255)
    number = models.CharField("Телефон", default="", max_length=255)

    def save(self, *args, **kwargs):
        # Хешируем пароль перед сохранением объекта
        self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Trainer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("ФИО", default="", max_length=255)
    email = models.CharField(verbose_name="Email", max_length=255, default="")
    skills = models.CharField(verbose_name="Навыки", max_length=255)
    password = models.CharField(max_length=255)
    number = models.CharField("Телефон", default="", max_length=255)

    def save(self, *args, **kwargs):
        # Хешируем пароль перед сохранением объекта
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
