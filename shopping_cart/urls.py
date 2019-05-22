from django.urls import path

from . import views


app_name = 'shopping_cart'

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<int:item_id>/', views.add_to_cart, name='add_to_cart')
]