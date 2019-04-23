from django.urls import path

from . import views


app_name = 'shirts'

urlpatterns = [
    path('', views.shirts, name='shirts'),
    path('detail/<int:sid>/', views.shirts_detail, name='shirts_detail'),
]