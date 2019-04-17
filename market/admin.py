from django.contrib import admin

from .models import Categories, Products, Shirt, ShirtMaterial, ShirtOptions


admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Shirt)
admin.site.register(ShirtMaterial)
admin.site.register(ShirtOptions)