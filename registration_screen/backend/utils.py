from django.http import HttpResponseRedirect

from registration_screen.models import Student


def create_user_from_registration_screen(request):
    full_name = request.POST.get('username')
    email_or_phone = request.POST.get('email_or_phone')
    password = request.POST.get('password')

    # Создаем объект в базе данных
    if "@" in email_or_phone:
        Student.objects.create(
            name=full_name,
            email=email_or_phone,
            password=password
        )
    else:
        Student.objects.create(
            name=full_name,
            number=email_or_phone,
            password=password
        )

    # Перенаправляем пользователя на другую страницу после регистрации
    # TODO: Пока что стоит заглушка
    return HttpResponseRedirect('/main_screen')
