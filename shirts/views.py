from django.shortcuts import render

from .models import Shirt


def shirts(request):
    shirts = Shirt.objects.all()
    context = {'shirts': shirts}
    return render(request, 'shirts/shirts.html', context)


