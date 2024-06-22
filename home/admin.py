from django.contrib import admin
from home.models import Books, custumber, Sports
from home.models import Product

# Register your models here.
admin.site.register(custumber)
admin.site.register(Product)
admin.site.register(Books)
admin.site.register(Sports)
