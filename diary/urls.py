from django.urls import path
from . import views


app_name = 'diary'
urlpatterns = [
        path('', views.home, name='home'),
        path('add/', views.add, name='add'),
        ]
