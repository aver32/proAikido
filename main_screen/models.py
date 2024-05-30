from django.db import models

from registration_screen.models import User


class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    schedule_date = models.DateField()
    schedule_time_start = models.TimeField()
    schedule_time_end = models.TimeField()
    trainer_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trainer_schedules')
    student_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_schedules')

