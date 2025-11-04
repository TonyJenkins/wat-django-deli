from django.urls import path

from . import views

app_name = 'cheese_counter'

urlpatterns = [
    path('<slug:slug>', views.cheese_detail, name='cheese_detail'),
]
