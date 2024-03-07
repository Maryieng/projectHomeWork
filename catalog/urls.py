from django.urls import path

from catalog.views import ProductListView, ProductDetailView, ProductView

app_name = 'shop'
urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ProductView.as_view(), name='contacts'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_info'),
]
