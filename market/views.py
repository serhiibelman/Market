from django.shortcuts import render, get_object_or_404

from .models import Categories, Products


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
        'products': products,
        # 'cname': cname
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


def test(request):
    return render(request, 'market/cart.html', context)