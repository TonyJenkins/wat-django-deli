from django.urls import path

from . import views

app_name = 'cheese_counter'

urlpatterns = [
    path('', views.cheese_list, name='cheese_list'),
    path('vegan', views.vegan, name='vegan_cheese_list'),
    path('<slug:slug>', views.cheese_detail, name='cheese_detail'),
]
