from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpRequest

from registration_screen.models import User, UserType


def create_user_from_registration_screen(request: HttpRequest):
    full_name = request.POST.get('username')
    email_or_phone = request.POST.get('email_or_phone')
    password = request.POST.get('password')
    is_student = request.POST.get('studentCheck')
    user_type = UserType.STUDENT if is_student else UserType.TRAINER

    # Создаем объект тренера или студента в базе данных
    if "@" in email_or_phone:
        user = User.objects.create(
            name=full_name,
            email=email_or_phone,
            password=password,
            user_type=user_type
        )
    else:
        user = User.objects.create(
            name=full_name,
            number=email_or_phone,
            password=password,
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
            current_user = User.objects.get(email=email_or_phone)
        else:
            current_user = User.objects.get(number=email_or_phone)
    except User.DoesNotExist:
        messages.error(request, "Пользователь не найден, неверный email или номер телефона")
        return render(request, 'registration_screen/login.html')

    if current_user is not None and current_user.check_password(password):
        request.session['current_user_id'] = current_user.id
        return redirect('/main_screen')
    else:
        messages.error(request, "Неверный пароль")
        return render(request, 'registration_screen/login.html')
