from django.contrib import admin


from catalog.models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    list_filter = ('category_name',)
    search_fields = ('category_name', 'category_description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'сategory')
    list_filter = ('сategory',)
    search_fields = ('product_name', 'description',)
