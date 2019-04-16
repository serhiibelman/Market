from django.urls import path
from . import views


app_name = 'market'

urlpatterns = [
    path('', views.main, name='main'),
    path('cart/', views.cart, name='cart'),
    path('prods/<str:cname>/', views.prods, name='prods'),
    path('prods/<str:cname>/<int:pid>/', views.prods_detail, name='prods_detail'),
    path('merch/<str:cname>/', views.merch, name='merch'),
    path('merch/<str:cname>/<int:sid>/', views.merch_detail, name='merch_detail'),
]
