from django.shortcuts import render

from registration_screen.models import User, UserType


# Create your views here.
def show_students(request):
    students = User.objects.filter(user_type=UserType.STUDENT)

    return render(
        request,
        'students/students.html'
    )