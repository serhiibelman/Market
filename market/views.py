from django.shortcuts import render, get_object_or_404

from .models import Merch, MerchColor, MerchMaterial, MerchSize, MerchView


def main(request):
    merch = Merch.objects.all()
    context = {'merch': merch}
    return render(request, 'market/main.html', context)


def merch_detail(request, mid, color=None):
    prods = MerchView.objects.filter(id=mid)
    colors = []
    materials = []
    sizes = []

    for prod in prods:
        colors.append(prod.get_color())
        materials.append(prod.material)
        sizes.append(prod.size)
        title = prods.title
        image = prods.image
        de
    
    if color:
        prods = MerchView.objects.filter(id=mid).filter(color=color)
    else:
        prods = MerchView.objects.filter(id=mid).filter(color=colors[0])
    
    context = {
         'prods': prods,
         'title': prods[0].title,
         'image': prods[0].image,
         'colors': set(colors),
         'materials': set(materials),
         'sizes': set(sizes)
    }
    return render(request, 'market/merch_detail.html', context)


def cart(request):
    merch = Merch.objects.filter(in_cart=True)
    if request.method == 'POST':
        mid = request.POST['remove']
        merch = Merch.objects.get(id=mid)
        merch.in_cart = False
        merch.save()
    context = {
        'merch': merch
    }
    return render(request, 'market/cart.html', context)
