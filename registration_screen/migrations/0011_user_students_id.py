# Generated by Django 5.0.4 on 2024-05-26 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_screen', '0010_alter_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='students_id',
            field=models.TextField(blank=True, default='[]', verbose_name='ID учеников'),
        ),
    ]
