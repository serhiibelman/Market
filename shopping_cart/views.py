from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse

from mailauth.models import User
from shirts.models import Shirt
from .models import OrderItem, Order
from .extras import generate_order_id


def cart(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'shopping_cart/cart.html', context)


def add_to_cart(request, **kwargs):
    user_profile = get_object_or_404(User, id=request.user.id)
    material = request.GET['material']
    size = request.GET['size']
    shirt = Shirt.objects.get(group=group, size=size, material=material)
    order_item, status = OrderItem.objects.get_or_create(product=shirt)
    print(order_item, status)
    user_order, status= Order.objects.get_or_create(owner=user_profile)
    print(user_order, status)
    if status:
        user_order.ref_code = generate_order_id()
        user_order.save()
    messages.info(request, 'item added to cart')
    kwargs = {'slug': shirt.group.slug, 'color': shirt.color}
    return redirect(reverse('shirts:shirt_card', kwargs=kwargs))