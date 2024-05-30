from django.urls import path
from . import views

urlpatterns = [
    path('show_trainers', views.show_trainers)
]