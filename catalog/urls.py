from django.urls import path

from catalog.views import index, contacts, product_info

app_name = 'shop'
urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('<int:pk>/', product_info, name='product_info'),
]
