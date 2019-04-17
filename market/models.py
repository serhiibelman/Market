from django.db import models

from .constants import LABELS, SIZES, MATERIALS, COLORS


class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.CharField(max_length=250)
    label = models.CharField(max_length=1, choices=LABELS)

    def __str__(self):
        return '{}'.format(self.name)


class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.CharField(max_length=250)
    description = models.TextField()
    in_cart = models.BooleanField(default=False)

    def __str__(self):
        return '{} - ${}'.format(self.title, self.price)


class Shirt(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.CharField(max_length=250)
    description = models.TextField()
    in_cart = models.BooleanField(default=False)

    def __str__(self):
        return '{} - ${}'.format(self.title, self.price)


class ShirtMaterial(models.Model):
    shirt = models.ForeignKey(Shirt, on_delete=models.CASCADE)
    price_coef = models.FloatField(default=0)
    material = models.CharField(max_length=15, choices=MATERIALS)

    def get_material(self):
        for mtrl in MATERIALS:
            if mtrl[0] == self.material:
                return mtrl[1]
        return None

    def __str__(self):
        return '{} | {} - ${}'.format(
            self.shirt.title,
            self.get_material(),
            self.price_coef
        )


class ShirtOptions(models.Model):
    material = models.ForeignKey(ShirtMaterial, on_delete=models.CASCADE)
    size = models.CharField(max_length=1, choices=SIZES)
    color = models.CharField(max_length=7, choices=COLORS)

    def get_color(self):
        for clr in COLORS:
            if clr[0] == self.color:
                return clr[1]
        return None

    def __str__(self):
        print(self.size)
        return '{}'.format(self.size)
