from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from apps.shop.models import Category, Ingredient, Product
from apps.promotions.models import PromotionArticle


class MySitemap(Sitemap):
    protocol = "https"


class CategorySitemap(MySitemap):
    def items(self):
        return Category.objects.filter(is_enabled=True)


class IngredientSitemap(MySitemap):
    def items(self):
        return Ingredient.objects.filter(is_enabled=True)


class ProductSitemap(MySitemap):
    def items(self):
        return Product.objects.filter(is_enabled=True)


class PromotionArticleSitemap(MySitemap):
    def items(self):
        return PromotionArticle.objects.filter(is_enabled=True)


class StaticViewSitemap(MySitemap):

    def items(self):
        return (
            'home',
            'contacts:contacts',
            'promotions:list'
        )

    def location(self, item):
        return reverse(item)
