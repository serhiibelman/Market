from django.shortcuts import render, get_object_or_404

from .models import Shirt


def shirts(request):
    shirts = Shirt.objects.all()
    context = {'shirts': shirts}
    return render(request, 'shirts/shirts.html', context)


def shirts_detail(request, sid):
    shirt = get_object_or_404(Shirt, id=sid)
    context = {'shirt': shirt}
    return render(request, 'shirts/shirts-detail.html', context)
