from django.shortcuts import render

from catalog.models import Product


def home(request):
    context_list = {'object_list': Product.objects.all()}

    return render(request, 'main/home.html', context=context_list)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Name: {name}, Phone: {phone}, Message: {message}')
    return render(request, 'main/contacts.html')


def product_info(request, pk):
    category_item = {'object': Product.objects.get(pk=pk)}

    return render(request, 'main/product_info.html', context=category_item)
