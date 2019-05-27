from django.urls import path
from . import views


app_name = 'todo'
urlpatterns = [
        path('',views.index, name='index'),
        path('deleteComplete', views.deleteComplete, name='deleteComplete'),
        path('del', views.deleteAll, name='deleteAll'),
        path('add', views.add, name='add'),
        path('complete/<id>', views.complete, name='complete'),

        ]
