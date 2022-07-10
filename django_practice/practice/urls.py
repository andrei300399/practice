from django.urls import path

from . import views

app_name = 'practice'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_post/', views.add_post, name='add_post'),
    path('delete_post/<post_id>/', views.delete_post, name='delete_post'),
]