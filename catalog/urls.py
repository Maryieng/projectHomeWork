from django.urls import path

from catalog.views import home, contacts, product_info

app_name = 'shop'
urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/', product_info, name='product_info'),
]
