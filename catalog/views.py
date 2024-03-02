from django.shortcuts import render

from catalog.models import Product


def index(request):

    return render(request, 'main/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Name: {name}, Phone: {phone}, Message: {message}')
    return render(request, 'main/contacts.html')


def product_info(request, pk):
    category_item = {'object': Product.objects.get(pk=pk)}

    return render(request, 'catalog/product_detail.html', category_item)


def whole_list(request):
    context_list = {'object_list': Product.objects.all()}

    return render(request, 'catalog/product_list.html', context_list)
