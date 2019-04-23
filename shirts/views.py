from django.shortcuts import render, get_object_or_404

from .models import Shirt


def shirts(request):
    shirts = Shirt.objects.filter(as_group_title=True)
    context = {'shirts': shirts}
    return render(request, 'shirts/shirts.html', context)


def shirts_detail(request, sid, color, material):
    shirt = get_object_or_404(Shirt, id=sid, color=color, material=material)
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
