from django.shortcuts import render
from django.http import HttpResponse


def profile_screen(request):
    return render(request, 'profile_screen/my_profile.html')
