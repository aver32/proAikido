from django.contrib import messages
from django.shortcuts import render
from registration_screen.backend.utils import create_user_from_registration_screen, authorization


def registration(request):
    if request.method == 'POST':
        return create_user_from_registration_screen(request)
    return render(request, 'registration_screen/registration.html')


def login(request):
    if request.method == 'POST':
        return authorization(request)
    return render(request, 'registration_screen/login.html')

