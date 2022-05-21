from django.urls import path

from . import views

app_name = 'Photo'

urlpatterns = [
    path('', views.home, name="home"),
]
