from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from apps.shop.models import Category, Ingredient, Product


class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.filter(is_enabled=True)


class IngredientSitemap(Sitemap):
    def items(self):
        return Ingredient.objects.filter(is_enabled=True)


class ProductSitemap(Sitemap):
    def items(self):
        return Product.objects.filter(is_enabled=True)


class StaticViewSitemap(Sitemap):

    def items(self):
        return (
            'home',
            'contacts:contacts'
        )

    def location(self, item):
        return reverse(item)
