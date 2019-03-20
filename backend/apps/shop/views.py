from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views.decorators.http import require_POST
from django.http import JsonResponse, Http404
from django.contrib import messages
from django.conf import settings
from django.shortcuts import redirect, reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Ingredient, Product, Order, CartProduct, DeliverySettings
from .utils import create_robokassa_url, send_order_email_to_client
import json
from hashlib import sha512


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

    # Сообщение об успехе, отправление E-Mail
    if o.pay_mode == 'self':
        messages.add_message(
            request,
            messages.SUCCESS,
            'Заказ успешно создан. Менеджер свяжется с вами в ближайшее время.'
        )
        send_order_email_to_client(o)

    # Данные в ответе
    response_data = {
        'success': 1,
        'unique_id': o.unique_id
    }

    # Ссылка на оплату в Robokassa
    if o.pay_mode == 'online':
        response_data['robokassa_url'] = create_robokassa_url(o)

    return JsonResponse(response_data)


@require_POST
@csrf_exempt
def robokassa_result(request):
    """Обрабатывает успешный результат оплаты на Robokassa."""
    # Пароль Robokassa
    mrh_pass2 = settings.ROBOKASSA_TEST_PASSWORD2 if settings.ROBOKASSA_IS_TEST else settings.ROBOKASSA_PASSWORD2

    # Параметры, которые отправил Robokassa
    out_summ = request.POST.get('OutSum')
    inv_id = request.POST.get('InvId')
    crc = request.POST.get('SignatureValue')

    # Построение хэша
    my_crc = sha512(f"{out_summ}:{inv_id}:{mrh_pass2}".encode('utf-8')).hexdigest().upper()

    # Если хеши совпали
    if my_crc == crc:
        order = Order.objects.get(pk=inv_id)
        order.paid = True
        order.save()
        send_order_email_to_client(order)
        return JsonResponse({'success': 1})
    else:
        return JsonResponse({'error': 1})


def robokassa_success(request):
    """Обрабатывает переадресацию с Robokassa в случае успешного платежа."""
    # Пароль Robokassa
    mrh_pass1 = settings.ROBOKASSA_TEST_PASSWORD1 if settings.ROBOKASSA_IS_TEST else settings.ROBOKASSA_PASSWORD1

    # Параметры, которые отправил Robokassa
    out_summ = request.GET.get('OutSum')
    inv_id = request.GET.get('InvId')
    crc = request.GET.get('SignatureValue')

    # Построение хэша
    my_crc = sha512(f"{out_summ}:{inv_id}:{mrh_pass1}".encode('utf-8')).hexdigest()

    if my_crc == crc:
        order = Order.objects.get(pk=inv_id)
        if order.paid:
            messages.add_message(
                request,
                messages.SUCCESS,
                'Заказ успешно создан. Менеджер свяжется с вами в ближайшее время.'
            )
            return redirect(reverse('shop:order-detail', args=[order.unique_id]))
        else:
            raise Http404('order hasn\'t been paid!')
    else:
        raise Http404('bad sign')


def robokassa_fail(request):
    """Обрабатывает переадресацию с Robokassa в случае неуспешного платежа."""
    return redirect('/')


class OrderDetailView(DetailView):
    """Страница заказа."""
    model = Order
    template_name = 'shop/order_detail/order_detail.html'
    slug_url_kwarg = 'unique_id'
    slug_field = 'unique_id'
