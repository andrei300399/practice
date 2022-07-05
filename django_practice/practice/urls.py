from django.urls import path

from . import views

app_name = 'practice'

urlpatterns = [
    path(r'', views.index, name='index'),
]