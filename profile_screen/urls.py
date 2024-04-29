from django.urls import path
from . import views

urlpatterns = [
    path('profile_screen', views.profile_screen),
    path('edit_profile', views.edit_profile),
    path('update_user_profile/', views.update_user_profile, name='update_user_profile'),
]