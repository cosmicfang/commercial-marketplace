from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )  # order item name according to name
        verbose_name_plural = "Categories"  # string representation of class 

    def __str__(self):
        return self.name   # name of the catrgories, we show the name as the values in name
    

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  #Django will automatically add the date and time

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Items"

    def __str__(self):
        return self.name