from django.urls import path
from . import views

urlpatterns = [
    path('main_screen', views.main)
]