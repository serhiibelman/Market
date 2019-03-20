from django.shortcuts import render, get_object_or_404

from .models import Categories, Products


def main(request):
    categories = Categories.objects.all()
    context = {'categories': categories}
    return render(request, 'market/main.html', context)


def prods(request, cname):
    products = Products.objects.filter(category__name=cname)
    context = {
        'products': products,
        'cname': cname
    }
    return render(request, 'market/prods.html', context)


def prods_detail(request, cname, pid):
    product = get_object_or_404(Products, id=pid)
    context = {'product': product}
    return render(request, 'market/prods_detail.html', context)
