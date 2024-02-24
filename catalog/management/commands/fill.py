from django.core.management import BaseCommand
import json
from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open('data.json', encoding='utf-8') as json_file:
            data = json.load(json_file)

            product_for_create = []
            category_for_create = []

            for category in data:
                if category["model"] == "catalog.category":
                    category_for_create.append(Category(category_name=category["fields"]['category_name'],
                                                        category_description=category["fields"]['category_description']))
            Category.objects.bulk_create(category_for_create)
            for product in data:
                if product["model"] == "catalog.product":
                    product_for_create.append(Product(product_name=product["fields"]['product_name'],
                                                      description=product["fields"]['description'],
                                                      сategory=Category.objects.filter(pk=product["pk"]),
                                                      price=product["fields"]['price']))

            Product.objects.bulk_create(product_for_create)
