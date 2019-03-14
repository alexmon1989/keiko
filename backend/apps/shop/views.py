from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib import messages
from .models import Category, Ingredient, Product, Order, CartProduct, DeliverySettings
import json


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Связанные продукты
        if self.object.related_products.filter(is_enabled=True).count() > 0:
            context['related_products'] = self.object.related_products.filter(is_enabled=True)
        else:
            context['related_products'] = Product.objects.filter(
                primary_category=self.object.primary_category,
                is_enabled=True
            ).exclude(pk=self.object.pk)
        return context


class CartView(TemplateView):
    """Страница корзины."""
    template_name = 'shop/cart/cart_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        delivery_settings, created = DeliverySettings.objects.get_or_create()
        # Настройки доставки
        if delivery_settings.product:
            context['delivery_price'] = delivery_settings.product.price
        else:
            context['delivery_price'] = 100
        context['delivery_discount_from'] = delivery_settings.price_discount_from
        return context


@require_POST
def create_order(request):
    """Обрабатывает запрос на заказ."""
    # Получение данных запроса
    data = json.loads(request.body.decode('utf-8'))

    # Создание заказа
    o = Order(
        delivery_mode=data.get('deliveryMode', None),
        pay_mode=data.get('payMode', None),
        user_name=data.get('username', None),
        user_phone=data.get('userphone', None),
        user_email=data.get('useremail', None),
        user_address=data.get('useraddress', None),
        user_comment=data.get('usercomment', None),
    )
    o.save()
    for product in data.get('cart', []):
        c_p = CartProduct(
            order=o,
            product_id=product['id'],
            price=product['price'],
            count=product['count'],
        )
        c_p.save()

    # Сообщение об успехе
    messages.add_message(request, messages.SUCCESS, 'Заказ успешно создан. Менеджер свяжется с вами в ближайшее время.')

    # Ответ
    return JsonResponse({
        'success': 1,
        'unique_id': o.unique_id
    })


class OrderDetailView(DetailView):
    """Страница заказа."""
    model = Order
    template_name = 'shop/order_detail/order_detail.html'
    slug_url_kwarg = 'unique_id'
    slug_field = 'unique_id'
