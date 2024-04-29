from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from registration_screen.models import User, UserType


def create_user_from_registration_screen(request):
    full_name = request.POST.get('username')
    email_or_phone = request.POST.get('email_or_phone')
    password = request.POST.get('password')
    is_student = request.POST.get('studentCheck')
    user_type = UserType.STUDENT if is_student else UserType.TRAINER

    # Создаем объект тренера или студента в базе данных
    if "@" in email_or_phone:
        User.objects.create(
            name=full_name,
            email=email_or_phone,
            password=password,
            user_type=user_type
        )
    else:
        User.objects.create(
            name=full_name,
            number=email_or_phone,
            password=password,
            user_type=user_type
        )

    # Перенаправляем пользователя на другую страницу после регистрации
    return redirect('/main_screen')

def authorization(request):
    email_or_phone = request.POST.get('email_or_phone')
    password = request.POST.get('password')

