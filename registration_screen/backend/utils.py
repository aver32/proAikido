from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.hashers import make_password

from registration_screen.models import User, UserType


def create_user_from_registration_screen(request: HttpRequest):
    full_name = request.POST.get('username')
    email_or_phone = request.POST.get('email_or_phone')
    password = request.POST.get('password')
    is_student = request.POST.get('studentCheck')
    user_type = UserType.STUDENT if is_student else UserType.TRAINER

    # Создаем объект тренера или студента в базе данных
    user = User.objects.create(
        name=full_name,
        number=email_or_phone if "@" not in email_or_phone else "",
        email=email_or_phone if "@" in email_or_phone else "",
        password=make_password(password),
        user_type=user_type
    )
    request.session['current_user_id'] = user.id

    # Перенаправляем пользователя на другую страницу после регистрации
    return redirect('/main_screen')


def authorization(request):
    email_or_phone = request.POST.get('email_or_phone')
    password = request.POST.get('password')

    try:
        if "@" in email_or_phone:
            current_user = User.objects.filter(email=email_or_phone).first()
        else:
            current_user = User.objects.filter(number=email_or_phone).first()
    except User.DoesNotExist:
        messages.error(request, "Пользователь не найден, неверный email или номер телефона")
        return render(request, 'registration_screen/login.html')
    if current_user is not None and current_user.check_password(password):
        request.session['current_user_id'] = current_user.id
        return redirect('/main_screen')
    else:
        messages.error(request, "Неверный пароль")
        return render(request, 'registration_screen/login.html')
