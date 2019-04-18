from django.contrib import admin

from .models import Merch, MerchColor, MerchMaterial, MerchSize


admin.site.register(Merch)
admin.site.register(MerchColor)
admin.site.register(MerchMaterial)
admin.site.register(MerchSize)