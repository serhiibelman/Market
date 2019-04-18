from django.urls import path
from . import views


app_name = 'market'

urlpatterns = [
    path('', views.main, name='main'),
    path('detail/<int:mid>/', views.merch_detail, name='merch_detail'),
    path('cart/', views.cart, name='cart'),
]
