from django.db import models


# Create your models here.
class custumber(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.name


# models.py


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    on_sale = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to="products/", null=True, blank=True
    )  # Specify upload directory

    def __str__(self):
        return self.name


class Books(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    on_sale = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to="books/", null=True, blank=True
    )  # Specify upload directory

    def __str__(self):
        return self.name


class Sports(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    on_sale = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to="sports/", null=True, blank=True
    )  # Specify upload directory

    def __str__(self):
        return self.name
