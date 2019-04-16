from django.db import models


LABELS = (
    ('1', 'Cars'),
    ('2', 'Merch')
)

SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large')
)

MATERIALS = (
    ('1', 'cotton'),
    ('2', 'flax')
)

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
    price_coef = models.FloatField()
    material = models.CharField(max_length=15, choices=MATERIALS)

    def __str__(self):
        return '{} - ${}'.format(self.material, self.price_coef)


class ShirtSize(models.Model):
    material = models.ForeignKey(ShirtMaterial, on_delete=models.CASCADE)
    size = models.CharField(max_length=1, choices=SIZES)

    def __str__(self):
        return '{}'.format(self.size)
