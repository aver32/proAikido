from django.shortcuts import render
import datetime
from django.views.decorators.cache import never_cache


@never_cache
def main_screen(request):
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
        row.append(time_slots[i])  # В первую колонку добавляем временные промежутки
        for j in range(7):
            row.append("+")  # Добавляем дни недели в остальные колонки
        table_data.append(row)

    context = {
        'table_data': table_data,
    }

    return render(request, 'main_screen/main.html', context)
