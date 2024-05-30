from time import timezone

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import never_cache

from main_screen.backend.utils import *
from main_screen.models import Schedule


@never_cache
def main_screen(request):
    context = {
        'table_data': create_table_with_class(request),
        'students': get_students_from_db()
    }

    return render(request, 'main_screen/main.html', context)


@never_cache
def save_data(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        time_to_training = request.POST.get('time')
        start_time_str, end_time_str = time_to_training.split(" - ")
        student = User.objects.get(id=student_id)
        trainer = User.objects.get(id=request.session['current_user_id'])

        Schedule.objects.create(
            schedule_date=get_schedule_date(request),
            schedule_time_start=datetime.datetime.strptime(start_time_str, "%H:%M"),
            schedule_time_end=datetime.datetime.strptime(end_time_str, "%H:%M"),
            trainer_id=trainer,
            student_id=student
        )
        context = {
            'table_data': create_table_with_class(request),
            'students': get_students_from_db()
        }
        return render(request, 'main_screen/main.html', context)
    else:
        return JsonResponse({'error': 'Метод запроса не поддерживается.'}, status=405)

@never_cache
def delete_data(request):
    if request.method == 'POST':
        time_to_training = request.POST.get('time')
        start_time_str, end_time_str = time_to_training.split(" - ")
        trainer = User.objects.get(id=request.session['current_user_id'])
        Schedule.objects.filter(
            schedule_date=get_schedule_date(request),
            schedule_time_start=datetime.datetime.strptime(start_time_str, "%H:%M"),
            schedule_time_end=datetime.datetime.strptime(end_time_str, "%H:%M"),
            trainer_id=trainer,
        ).delete()
        context = {
            'table_data': create_table_with_class(request),
            'students': get_students_from_db()
        }
        return render(request, 'main_screen/main.html', context)
    else:
        return JsonResponse({'error': 'Метод запроса не поддерживается.'}, status=405)


def get_schedule_date(request):
    # Получение текущей даты и времени
    current_date = datetime.datetime.now()

    index_of_day = int(request.POST.get('column')) - 2
    print(index_of_day)

    # Определение первого дня текущей недели (понедельника)
    start_of_week = current_date - datetime.timedelta(days=current_date.weekday())

    # Расчет даты на текущей неделе, соответствующей указанному дню недели
    schedule_date = start_of_week + datetime.timedelta(days=index_of_day)

    return schedule_date
