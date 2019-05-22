from django.urls import path

from . import views


app_name = 'shirts'

urlpatterns = [
    path('', views.shirts, name='shirts'),
    path('detail/<slug:slug>/<str:color>/', views.shirts_card, name='shirts_card'),
    path('create/', views.add_shirt, name='add_shirt'),
]