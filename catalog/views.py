from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductView(View):
    def get(self, request):
        return render(request, 'shop:contacts')

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Name: {name}, Phone: {phone}, Message: {message}')
        return render(request, 'shop:contacts')


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('product_name', 'description', 'preview', 'category', 'price')
    success_url = reverse_lazy('shop:list_products')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('product_name', 'description', 'preview', 'category', 'price')
    success_url = reverse_lazy('shop:list_products')

