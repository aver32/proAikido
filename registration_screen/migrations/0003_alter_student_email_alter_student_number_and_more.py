# Generated by Django 5.0.4 on 2024-04-21 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_screen', '0002_alter_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(default='', max_length=255, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='student',
            name='number',
            field=models.CharField(default='', max_length=255, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='email',
            field=models.CharField(default='', max_length=255, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='number',
            field=models.CharField(default='', max_length=255, verbose_name='Телефон'),
        ),
    ]
