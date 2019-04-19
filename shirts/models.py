from django.db import models

from market.constants import COLORS, SIZES, MATERIALS


class Shirt(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    price = models.FloatField()
    color = models.CharField(max_length=7, choices=COLORS)
    material = models.CharField(max_length=15, choices=MATERIALS)
    size = models.CharField(max_length=1, choices=SIZES)
    description = models.TextField()
    in_cart = models.BooleanField(default=False)

    def get_material(self):
        for mtrl in MATERIALS:
            if mtrl[0] == self.material:
                return mtrl[1]
        return None

    def get_color(self):
        for clr in COLORS:
            if clr[0] == self.color:
                return clr[1]
        return None

    def __str__(self):
    	return '{}'.format(self.title)
    

