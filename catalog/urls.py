from django.urls import path

from catalog.views import index, contacts, product_info

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('products_info/', product_info),
]
