from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[
        ('Clothing', 'Clothing'),
        ('Groceries', 'Groceries'),
    ])
    size_or_weight = models.CharField(max_length=10, choices=[], blank=True)


    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        if self.category == 'Clothing':
            self._set_clothing_choices()
        elif self.category == 'Groceries':
            self._set_groceries_choices()

    def _set_clothing_choices(self):
        self._meta.get_field('size_or_weight').choices = [
            ('2xl', '2XL'),
            ('4xl', '4XL'),
        ]

    def _set_groceries_choices(self):
        self._meta.get_field('size_or_weight').choices = [
            ('500g', '500g'),
            ('1kg', '1kg'),
        ]

    def _str_(self):
        return self.name



class Cart(models.Model):
    user = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.user
    