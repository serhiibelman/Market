from django.urls import path

from . import views


app_name = 'shirts'

urlpatterns = [
    path('', views.shirts, name='shirts'),
    path('detail/<int:sid>/<str:color>/<str:material>/', views.shirts_detail, name='shirts_detail'),
]