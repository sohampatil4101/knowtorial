from django.contrib import admin
from django.urls import path
from apii.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # API for adding product
    path('api/product', addproduct),

    # API for getting product with its primary key 'id'
    path('api/product/<int:pk>', getproduct),

    # add product to cart
    path('api/cart', addcart)
]

