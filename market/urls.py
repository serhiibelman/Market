from django.urls import path
from . import views


app_name = 'market'

urlpatterns = [
    path('', views.main, name='main'),
    path('cart/', views.cart, name='cart'),
    path('prods/<str:cname>/', views.prods, name='prods'),
    path('<str:cname>/<int:pid>/', views.prods_detail, name='prods_detail'),
]
