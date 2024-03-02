from django.urls import path

from catalog.views import index, contacts, product_info

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('/product_info/<int:pk>', product_info, name='product_info'),
]
