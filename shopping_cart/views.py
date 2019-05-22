from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse

from mailauth.models import User
from shirts.models import Shirt
from .models import OrderItem, Order


def cart(request):
    context = {}
    return render(request, 'shopping_cart/cart.html', context)


def add_to_cart(request, **kwargs):
    profile = get_object_or_404(User, user=request.user)
    shirt = get_object_or_404(Shirt, id=kwargs.get('item_id'))
    print(shirt)
    kwargs = {'slug': shirt.group.slug, 'color': shirt.color}
    return redirect(reverse('shirts:shirt_card', kwargs=kwargs))