from django.db import models, transaction
from django.db.models.signals import pre_save
from django.utils.text import slugify

from market.constants import COLORS, SIZES, MATERIALS


def upload_location(instance, filename):
    return 'img/shirts/{}'.format(filename)


class Group(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Shirt(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    is_group_title = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        upload_to=upload_location
    )
    price = models.FloatField()
    color = models.CharField(max_length=7, choices=COLORS)
    material = models.CharField(max_length=15, choices=MATERIALS)
    size = models.CharField(max_length=1, choices=SIZES)
    description = models.TextField()
    in_cart = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.title)

    @transaction.atomic
    def save(self, *args, **kwargs):
        if self.is_group_title:
            Shirt.objects.filter(is_group_title=True).update(is_group_title=False)
        super(Shirt, self).save(*args, **kwargs)

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

    def get_absolute_url(self):
        from django.urls import reverse
        kwargs = {'slug': self.group.slug, 'color': self.color}
        return reverse('shirts:shirts_detail', kwargs=kwargs)


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Shirt.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = '{}-{}'.format(
            slug,
            qs.first().id
        )
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_shirt_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_shirt_receiver, sender=Shirt)

    

