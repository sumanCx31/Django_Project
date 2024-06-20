from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
  path("",views.index, name='home'),
  path("contact",views.contact, name='contact'),
  path("about",views.about, name='about'),
  path("onsale",views.onsale, name='onsale'),
  path("order",views.order, name='order'),
  path("clothes",views.product_list, name='product_list'),
]