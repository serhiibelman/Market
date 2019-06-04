from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Group, Shirt, ShirtView
from .forms import GroupForm, ShirtForm
from mailauth.models import User
from shopping_cart.models import OrderItem, Order
from shopping_cart.extras import generate_order_id


def shirts(request):
    print(User.objects.all())
    shirts = Shirt.objects.filter(is_group_title=True)
    context = {'shirts': shirts}
    return render(request, 'shirts/shirts.html', context)


def shirts_card(request, slug, color):
    group = Group.objects.get(slug=slug)
    shirts = Shirt.objects.filter(group=group.id)
    materials = ShirtView.objects.filter(color=color).distinct()
    user_profile = get_object_or_404(User, id=request.user.id)

    colors = set()
    
    for shirt in shirts:
        colors.add(shirt.color)
    
    if request.method == 'POST':
        material = request.POST['material']
        size = request.POST['size']
        shirt = Shirt.objects.get(group=group, size=size, material=material)
        order_item, status = OrderItem.objects.get_or_create(product=shirt)
        print(order_item, status)
        user_order, status= Order.objects.get_or_create(owner=user_profile)
        user_order.items.add(order_item)
        print(user_order, status)
        if status:
            user_order.ref_code = generate_order_id()
            user_order.save()
        messages.info(request, 'item added to cart')      

    context = {
        'group': group,
        'shirts': shirts,
        'colors': colors,
        'materials': materials
    }
    return render(request, 'shirts/shirts-card.html', context)


# TODO: add permissions
def add_shirt(request):
    form = ShirtForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            # Create, but don't save the new Shirt instance.
            shirt = form.save(commit=False)
            shirt.save()
            return redirect('shirts:shirts')
    context = {
        'form': form
    }
    return render(request, 'shirts/add-shirt.html', context)