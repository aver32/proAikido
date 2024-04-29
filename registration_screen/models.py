from django.contrib.auth.hashers import make_password, check_password
from django.db import models


class UserType(models.IntegerChoices):
    TRAINER = 1, 'Тренер'
    STUDENT = 2, 'Студент'

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__.update(state)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("ФИО", default="", max_length=255)
    email = models.CharField(verbose_name="Email", max_length=255, default="")
    description = models.TextField(verbose_name="Описание", default="")
    skills = models.TextField(verbose_name="Навыки", max_length=255, default="")
    education = models.TextField(verbose_name="Образование", default="")
    achievements = models.TextField(verbose_name="Достижения", default="")
    club_address = models.TextField(verbose_name="Адрес клуба", default="г. Екатеринбург, ул. Мира 32")
    password = models.CharField(max_length=255)
    number = models.CharField("Телефон", default="", max_length=255)
    user_type = models.IntegerField("Тип пользователя", choices=UserType.choices, default=UserType.STUDENT)

    def save(self, *args, **kwargs):
        # Хешируем пароль перед сохранением объекта
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__.update(state)

