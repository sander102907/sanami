from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.forms import ModelForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import login, authenticate
import django_filters

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=30, blank=True)
    adress = models.CharField(max_length=30, blank=True)
    ZIP_code = models.CharField(max_length=6, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Product(models.Model):

    GENDER_CHOICES = (('MEN', 'Men'), ('WOMEN', 'Women'))
    CLOTHINGTYPE_CHOICES = (('SHOE', "Shoes"), ('CLOTHING', 'Clothes'))


    name = models.CharField(max_length = 100)
    image = models.FileField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField()
    clothingtype = models.CharField(choices = CLOTHINGTYPE_CHOICES, default="CLOTHING", max_length=8)
    gender = models.CharField(choices = GENDER_CHOICES, default="MEN", max_length=5)

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)

    class Meta:
        ordering = ('name',)

class ProductFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter()
    price__from = django_filters.NumberFilter(name='price', lookup_expr='from')
    price__to = django_filters.NumberFilter(name='price', lookup_expr='to')

    class Meta:
        model = Product
        fields = {'price': ['from', 'to'], }


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    class Meta:
        ordering = ('-created',)
