from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.forms import ProductForm, VersionForm, ModeratorProductForm, VersionFormSet
from catalog.models import Product, Version, Category
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from catalog.services import get_cached_categories, get_cached_products


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['products_list'] = get_cached_products()
        products = Product.objects.all()

        for product in products:
            versions = Version.objects.filter(product=product)
            active_versions = versions.filter(is_active=True)
            if active_versions:
                product.active_version = active_versions.last().name
            else:
                product.active_version = 'Нет активной версии'

        context_data['object_list'] = products
        return context_data



class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Контакты"
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Name: {name}, Phone: {phone}, Message: {message}")
        return super().get(request, *args, **kwargs)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    login_url = 'users:login'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        product = self.get_object()
        versions = Version.objects.filter(product=product)
        active_version = versions.filter(is_active=True).last()

        if active_version:
            product.active_version = active_version.name
        else:
            product.active_version = 'Нет активной версии'

        context_data['object'] = product
        return context_data


class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    login_url = 'users:login'
    form_class = ProductForm
    success_url = reverse_lazy('shop:list_products')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, formset=VersionFormSet, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()
        context_data['show_create_button'] = not self.request.user.groups.filter(name='moderator').exists()
        return context_data

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def test_func(self):
        return not self.request.user.groups.filter(name='moderator').exists()


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    login_url = 'users:login'
    form_class = ProductForm
    success_url = reverse_lazy('shop:list_products')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, formset=VersionFormSet, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
            context_data['request'] = self.request
            context_data['show_create_button'] = not self.request.user.groups.filter(name='moderator').exists()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_form_class(self):
        if self.request.user.has_perm('catalog.set_published') and not self.request.user.is_superuser:
            return ModeratorProductForm
        else:
            return ProductForm


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    login_url = 'users:login'
    success_url = reverse_lazy('shop:list_products')

    def test_func(self):
        return not self.request.user.groups.filter(name='moderator').exists()


class CategoryListView(ListView):
    model = Category

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['categories_list'] = get_cached_categories()
        return context_data
