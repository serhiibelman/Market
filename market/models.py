from django.db import models

from .constants import SIZES, MATERIALS, COLORS


class Merch(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return '{} - ${}'.format(self.title, self.price)


class MerchColor(models.Model):
    merch = models.ForeignKey(Merch, on_delete=models.CASCADE)
    color = models.CharField(max_length=7, choices=COLORS)

    def get_color(self):
        for clr in COLORS:
            if clr[0] == self.color:
                return clr[1]
        return None

    def __str__(self):
        return '{}'.format(self.get_color())


class MerchMaterial(models.Model):
    color = models.ForeignKey(MerchColor, on_delete=models.CASCADE)
    price_coef = models.FloatField(default=0)
    material = models.CharField(max_length=15, choices=MATERIALS)

    def get_material(self):
        for mtrl in MATERIALS:
            if mtrl[0] == self.material:
                return mtrl[1]
        return None

    def __str__(self):
        return '{} {} | {} - ${}'.format(
            self.color.merch.title,
            self.color.color,
            self.get_material(),
            self.price_coef
        )


class MerchSize(models.Model):
    material = models.ForeignKey(MerchMaterial, on_delete=models.CASCADE)
    size = models.CharField(max_length=5, choices=SIZES)
    in_cart = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.size)


class MerchView(models.Model):
    class Meta:
        managed = False
        db_table = 'merch_view'

    title = models.CharField(max_length=50)
    image = models.CharField(max_length=250)
    description = models.TextField()
    color = models.CharField(max_length=7, choices=COLORS)
    material = models.CharField(max_length=15, choices=MATERIALS)
    size = models.CharField(max_length=1, choices=SIZES)
    in_cart = models.BooleanField(default=False)
    price = models.FloatField()
    price_coef = models.FloatField()

    def get_color(self):
        for clr in COLORS:
            if clr[0] == self.color:
                return clr[1]
        return None