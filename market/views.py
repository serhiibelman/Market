from django.shortcuts import render, get_object_or_404

from .models import Categories, Products, Shirt, ShirtMaterial, ShirtOptions


def main(request):
    categories = Categories.objects.all()
    context = {'categories': categories}
    return render(request, 'market/main.html', context)

def cart(request):
    products = Products.objects.filter(in_cart=True)
    if request.method == 'POST':
        pid = request.POST['remove']
        product = Products.objects.get(id=pid)
        product.in_cart = False
        product.save()
    context = {
        'products': products
    }
    return render(request, 'market/cart.html', context)

def prods(request, cname):
    products = Products.objects.filter(category__name=cname)
    if request.method == 'POST':
        pid = request.POST['pid']
        product = Products.objects.get(id=pid)
        product.in_cart = True
        product.save()
        print(product.in_cart)
    context = {
        'products': products,
        'cname': cname
    }
    return render(request, 'market/prods.html', context)


def prods_detail(request, cname, pid):
    product = get_object_or_404(Products, id=pid)
    context = {'product': product}
    return render(request, 'market/prods_detail.html', context)


def merch(request, cname):
    shirts = Shirt.objects.filter(category__name=cname)
    print(shirts)
    if request.method == 'POST':
        pid = request.POST['pid']
        shirt = Shirt.objects.get(id=pid)
        shirt.in_cart = True
        shirt.save()
        print(shirt.in_cart)
    context = {
        'merch': shirts,
        'cname': cname
    }
    return render(request, 'market/merch.html', context)


def merch_detail(request, cname, pid):
    shirt = get_object_or_404(Shirt, id=pid)
    materials = ShirtMaterial.objects.filter(shirt=shirt.id)
    options = ShirtOptions.objects.filter(material__material='cotton')
    for option in options:
        print(option.get_color())
    context = {
         'shirt': shirt,
         'materials': materials,
         'options': options
    }
    return render(request, 'market/merch_detail.html', context)