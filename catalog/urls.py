from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CategoryListView

app_name = 'shop'
urlpatterns = [
    path('', cache_page(60)(ProductListView.as_view()), name='list_products'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_info'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('categories_list/', cache_page(60)(CategoryListView.as_view()), name='list_category'),
]
