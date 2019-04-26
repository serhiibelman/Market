from django.shortcuts import render, redirect, get_object_or_404

from .models import Group, Shirt
from .forms import GroupForm, ShirtForm


def shirts(request):
    shirts = Shirt.objects.filter(is_group_title=True)
    context = {'shirts': shirts}
    return render(request, 'shirts/shirts.html', context)


def shirts_detail(request, slug, color):
    group = Group.objects.get(slug=slug)
    shirts = Shirt.objects.filter(group=group.id)
    materials = Shirt.objects.filter(color=color)
    colors = set()
    
    for shirt in shirts:
        colors.add(shirt.color)
    
    context = {
        'group': group,
        'shirts': shirts,
        'colors': colors,
        'materials': materials
    }
    return render(request, 'shirts/shirts-detail.html', context)


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