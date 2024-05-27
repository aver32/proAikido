from django.urls import path
from . import views

urlpatterns = [
    path('show_prices', views.show_prices)
]