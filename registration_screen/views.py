from django.shortcuts import render
from registration_screen.backend.utils import create_user_from_registration_screen


def registration(request):
    if request.method == 'POST':
        return create_user_from_registration_screen(request)
    return render(request, 'registration.html')

