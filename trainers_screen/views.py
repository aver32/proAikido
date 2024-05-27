from django.shortcuts import render

from registration_screen.models import UserType, User


# Create your views here.
def show_trainers(request):
    trainers = User.objects.filter(user_type=UserType.TRAINER)

    middle_index = len(trainers) // 2

    return render(
        request,
        'trainers_screen/show_trainers.html',
        {
            'trainers': trainers,
            'middle_index': middle_index
        }
    )
