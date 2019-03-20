from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.CharField(max_length=250)

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
