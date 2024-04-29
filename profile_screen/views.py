from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse

from registration_screen.models import User, ProfileImageForm


def profile_screen(request):
    current_user_id = request.session.get('current_user_id')

    full_name = ""
    description = ""
    education = ""
    achievements = ""
    if current_user_id:
        # Получаем объект пользователя из базы данных
        current_user = User.objects.get(pk=current_user_id)
        full_name = current_user.name
        description = current_user.description
        education = current_user.education
        achievements = current_user.achievements
        return render(
            request,
            'profile_screen/my_profile.html',
            {
                'full_name': full_name,
                'description': description,
                "education": education,
                "achievements": achievements
            }
        )
    return redirect('login')


def edit_profile(request):
    current_user_id = request.session.get('current_user_id')

    full_name = ""
    description = ""
    education = ""
    achievements = ""
    number = ""
    email = ""
    club_address = ""
    if current_user_id:
        # Получаем объект пользователя из базы данных
        current_user = User.objects.get(pk=current_user_id)
        full_name = current_user.name
        number = current_user.number
        email = current_user.email
        club_address = current_user.club_address
        description = current_user.description
        education = current_user.education
        achievements = current_user.achievements
        return render(
            request,
            'profile_screen/edit_profile.html',
            {
                'full_name': full_name,
                "number": number,
                "email": email,
                "club_address": club_address,
                'description': description,
                "education": education,
                "achievements": achievements
            }
        )
    return redirect('login')


def update_user_profile(request):
    if request.method == 'POST':
        current_user_id = request.session.get('current_user_id')
        if current_user_id:
            # Получаем объект пользователя из базы данных
            current_user = get_object_or_404(User, id=current_user_id)
            # Сохранение фотки юзера в бд
            profile_form = ProfileImageForm(request.POST, request.FILES, instance=current_user)
            if profile_form.is_valid():
                profile_form.save()

            # Получаем данные из запроса
            full_name = request.POST.get('inputFullName')
            phone_number = request.POST.get('inputPhoneNumber')
            email = request.POST.get('inputEmail')
            club_address = request.POST.get('inputClubAddress')
            achievements = request.POST.get('inputAchievements')
            education = request.POST.get('inputEducation')
            description = request.POST.get('inputDescription')

            # Обновляем данные пользователя
            current_user.name = full_name
            current_user.number = phone_number
            current_user.email = email
            current_user.club_address = club_address
            current_user.achievements = achievements
            current_user.education = education
            current_user.description = description
            current_user.password = current_user.password

            current_user.save()

            # Отправляем ответ
            return redirect('/profile_screen')
        return redirect('login')

    # Если метод запроса не POST, возвращаем ошибку
    return JsonResponse({'error': 'Метод запроса должен быть POST'})

def logout(request):
    request.session['current_user_id'] = None
    return redirect('/login')
