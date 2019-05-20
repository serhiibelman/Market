from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shirts/', include('shirts.urls')),
    # path('cart/', include('shopping_cart.urls')),
]
