"""belajarmath URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from latihan.views import latihan
from materi.views import materi
from profil.views import profil
from vidiopembelajaran.views import vidiopembelajaran
from home.views import home 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('latihan/', latihan),
    path('materi/', materi),
    path('profil/', profil),
    path('vidiopembelajaran/', vidiopembelajaran),
    path('home/', home),
]
