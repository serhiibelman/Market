from django.shortcuts import render, get_object_or_404

from .models import Merch, MerchColor, MerchMaterial, MerchSize, MerchView


def main(request):
    merch = Merch.objects.all()
    context = {
        'merch': merch
    }
    return render(request, 'market/main.html', context)


def merch_detail(request, mid):
    prods = MerchView.objects.filter(id=mid)
    
    context = {
         'prods': prods
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
