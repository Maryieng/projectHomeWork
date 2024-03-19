from django.urls import path

from catalog.views import ProductListView, ProductDetailView, ProductView, ProductCreateView, ProductUpdateView

app_name = 'shop'
urlpatterns = [
    path('', ProductListView.as_view(), name='list_products'),
    path('contacts/', ProductView.as_view(), name='contacts'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_info'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
]
