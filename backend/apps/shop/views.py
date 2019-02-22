from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from .models import Category, Ingredient, Product


class CategoryDetailView(DetailView):
    """Страница категории."""
    model = Category
    queryset = Category.objects.filter(is_enabled=True)
    template_name = 'shop/category_detail/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object.product_set.filter(is_enabled=True).all()
        return context


class IngredientDetailView(DetailView):
    """Страница индгредиента."""
    model = Ingredient
    queryset = Ingredient.objects.filter(is_enabled=True)
    template_name = 'shop/ingredient_detail/ingredient_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object.product_set.filter(is_enabled=True).all()
        return context


class ProductDetailView(DetailView):
    """Страница продукта."""
    queryset = Product.objects.filter(is_enabled=True)
    template_name = 'shop/product_detail/product_detail.html'


class CartView(TemplateView):
    """Страница корзины."""
    template_name = 'shop/cart/cart_detail.html'
