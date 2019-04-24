from django.urls import path

from . import views


app_name = 'shirts'

urlpatterns = [
    path('', views.shirts, name='shirts'),
    path('detail/<str:slug>/', views.shirts_detail, name='shirts_detail'),
    path('create/', views.add_shirt, name='add_shirt'),
]