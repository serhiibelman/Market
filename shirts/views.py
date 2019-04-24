from django.shortcuts import render, redirect, get_object_or_404

from .models import Group, Shirt
from .forms import GroupForm, ShirtForm


def shirts(request):
    shirts = Shirt.objects.filter(is_group_title=True)
    context = {'shirts': shirts}
    return render(request, 'shirts/shirts.html', context)


def shirts_detail(request, slug):
    shirt = get_object_or_404(Shirt, slug=slug)
    shirts_group = Shirt.objects.filter(group=shirt.group)
    print(shirts_group)
    colors = set()
    sizes = set()
    materials = set()
    for obj in shirts_group:
        colors.add(obj.color)
        sizes.add(obj.size)
        materials.add(obj.material)
    
    context = {
        'shirt': shirt,
        'shirts_group': shirts_group,
        'colors': colors,
        'sizes': sizes,
        'materials': materials
    }
    return render(request, 'shirts/shirts-detail.html', context)


def add_shirt(request):
    form = ShirtForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        print('POST')
        if form.is_valid():
            # Create, but don't save the new Shirt instance.
            shirt = form.save(commit=False)
            shirt.save()
            print('saved')
            return redirect('shirts:shirts')
    context = {
        'form': form
    }
    return render(request, 'shirts/add-shirt.html', context)