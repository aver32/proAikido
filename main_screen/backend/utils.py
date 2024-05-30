import datetime

from main_screen.models import Schedule
from registration_screen.models import User, UserType


def get_students_from_db():
    return User.objects.filter(user_type=UserType.STUDENT)


def create_table_with_class(request):
    date_start = datetime.datetime.combine(datetime.date.today(), datetime.time(hour=10, minute=0))
    time_delta = datetime.timedelta(minutes=30)
    # Создаем список временных промежутков
    time_slots = []
    for i in range(24):
        date_end = date_start + time_delta
        time_slots.append(f"{date_start.strftime('%H:%M')} - {date_end.strftime('%H:%M')}")
        date_start += time_delta

    # Создаем список списков для таблицы
    table_data = []
    for i in range(24):
        row = []
        row.append(time_slots[i])
        for j in range(7):
            row.append("+")
        table_data.append(row)

    schedules = Schedule.objects.filter(trainer_id=request.session['current_user_id'])

    # Помечаем ячейки, в которых уже есть занятия
    for schedule in schedules:
        start_time = schedule.schedule_time_start

        time_slot_index = (start_time.hour - 9) * 2 + start_time.minute // 30
        day_of_week = schedule.schedule_date.weekday() + 1
        table_data[time_slot_index - 2][day_of_week] = User.objects.filter(id=schedule.student_id_id).first().name

    return table_data
