"""
URL configuration for proAikido project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import main_screen.views
import map_screen.views
import registration_screen.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profile_screen.urls')),
    path('', include('trainers_screen.urls')),
    path('', include('students.urls')),
    path('', include('prices.urls')),
    path('registration/', registration_screen.views.registration, name='registration'),
    path('login/', registration_screen.views.login, name='login'),
    path('maps/', map_screen.views.maps, name='maps'),
    path('main_screen/', main_screen.views.main_screen, name='main_screen'),
    path('', main_screen.views.main_screen, name='main_screen'),
    path('save/', main_screen.views.save_data, name='save_data'),
    path('delete/', main_screen.views.delete_data, name='delete_data'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
