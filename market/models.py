from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    picture = models.ImageField()
    description = models.TextField()
    in_cart = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}UAH'.format(self.title, self.price)