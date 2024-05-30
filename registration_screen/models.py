import json
from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django import forms


class UserType(models.IntegerChoices):
    STUDENT = 1, 'Студент'
    TRAINER = 2, 'Тренер'

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
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    students_id = models.TextField(verbose_name="ID учеников", blank=True, default="[]")
    groups_id = models.TextField(verbose_name="ID групп", blank=True, default="[]")

    def set_students_id(self, int_list):
        self.students_id = json.dumps(int_list)

    def get_students_id(self):
        return json.loads(self.students_id)

    def add_student_id(self, student_id):
        id_list = self.get_students_id()
        if student_id not in id_list:
            id_list.append(student_id)
            self.set_students_id(id_list)

    def remove_student_id(self, student_id):
        id_list = self.get_students_id()
        if student_id in id_list:
            id_list.remove(student_id)
            self.set_students_id(id_list)

    def set_groups_id(self, int_list):
        self.groups_id = json.dumps(int_list)

    def get_groups_id(self):
        return json.loads(self.groups_id)

    def add_group_id(self, group_id):
        id_list = self.get_groups_id()
        if group_id not in id_list:
            id_list.append(group_id)
            self.set_groups_id(id_list)

    def remove_group_id(self, group_id):
        id_list = self.get_groups_id()
        if group_id in id_list:
            id_list.remove(group_id)
            self.set_groups_id(id_list)

    def save(self, *args, **kwargs):
        # Хешируем пароль перед сохранением объекта
        #self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__.update(state)


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    schedule_str = models.TextField(verbose_name="Расписание", blank=True, default="Расписание отсутствует")


class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_image']
        # widgets = {
        #     'profile_image': forms.FileInput(attrs={
        #         'accept': 'image/*',
        #         'style': 'display:none;',  # Initially hide the input
        #     }),
        # }
