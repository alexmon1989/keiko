from django.shortcuts import reverse
from django.db import models
from django.core.mail import send_mail
from django.template import loader
from django.conf import settings
from keiko.utils import TimeStampedModel
from ckeditor.fields import RichTextField
import json
import uuid
from colorfield.fields import ColorField


class Category(TimeStampedModel):
    """Модель категории продукта."""
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField()
    weight = models.IntegerField('Вес', default=1000, help_text='Чем выше вес, тем выше элемент в списке категорий.')
    image = models.ImageField('Изображение', null=True, blank=True, help_text='Размер: 100px * 64px')
    is_enabled = models.BooleanField('Включено', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:category-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Property(TimeStampedModel):
    """Модель свойства продукта."""
    title = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Свойство'
        verbose_name_plural = 'Свойства'


class Ingredient(TimeStampedModel):
    """Модель свойства продукта."""
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField()
    weight = models.IntegerField('Вес', default=1000, help_text='Чем выше вес, тем выше элемент в списке ингредиентов.')
    image = models.ImageField('Изображение', null=True, blank=True, help_text='Размер: 100px * 64px')
    is_enabled = models.BooleanField('Включено', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:ingredient-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Product(TimeStampedModel):
    """Модель продукта."""
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField()
    image = models.ImageField('Изображение', null=True, blank=True, help_text='Размер: 450px * 450px')
    description = RichTextField('Описание', null=True, blank=True)
    primary_category = models.ForeignKey(Category, verbose_name='Первичная категория', blank=True, null=True,
                                         on_delete=models.SET_NULL, related_name='primary_category',
                                         help_text='Для блока "Хлебные крошки"')
    categories = models.ManyToManyField(Category, verbose_name='Категории', blank=True)
    properties = models.ManyToManyField(Property, verbose_name='Свойства', blank=True)
    ingredients = models.ManyToManyField(Ingredient, verbose_name='Ингредиенты', blank=True)
    price = models.FloatField('Цена', blank=True, null=True)
    related_products = models.ManyToManyField('Product', verbose_name='Связанные продукты', blank=True,
                                              help_text='Для блока "С этим продуктом часто покупают"')
    frontpad_id = models.PositiveIntegerField('id товара в системе Frontpad', null=True, blank=True)
    is_new = models.BooleanField('Новинка', default=False)
    is_spicy = models.BooleanField('Острое', default=False)
    is_hit = models.BooleanField('Хит', default=False)
    is_enabled = models.BooleanField('Включено', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:product-detail', kwargs={'slug': self.slug})

    def get_cart_data(self):
        res = {
            'id': self.pk,
            'title': self.title,
            'link': reverse('shop:product-detail', kwargs={'slug': self.slug}),
            'price': self.price
        }
        if self.image:
            res['img'] = self.image.url
        else:
            res['img'] = '/static/img/no-image.png'
        return json.dumps(res)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class CartProduct(TimeStampedModel):
    """Модель товара в корзине"""
    order = models.ForeignKey('Order', verbose_name='Заказ', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', verbose_name='Продукт', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.PositiveIntegerField('Цена')
    count = models.PositiveIntegerField('Количество')

    def __str__(self):
        if self.product:
            return self.product.title
        return 'Удалённый продукт'


class OrderStatus(TimeStampedModel):
    """Модель статуса заказа."""
    title = models.CharField('Название статуса', max_length=255)
    color = ColorField('Цвет', default='#FF0000')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class Order(TimeStampedModel):
    """Модель заказа."""
    unique_id = models.UUIDField('Уникальный идентификатор', default=uuid.uuid4, editable=False, unique=True)
    delivery_mode = models.CharField(
        'Способ доставки',
        max_length=255,
        choices=(('self', 'Самовывоз'), ('courier', 'Доставка курьером'))
    )
    pay_mode = models.CharField(
        'Метод оплаты',
        max_length=255,
        choices=(('cash', 'Наличными'),)
    )
    user_name = models.CharField('Имя клиента', max_length=255, null=True, blank=True)
    user_email = models.EmailField('E-Mail клиента', max_length=255, null=True, blank=True)
    user_phone = models.CharField('Телефон клиента', max_length=255, null=True, blank=True)
    user_address = models.CharField('Адрес доставки', max_length=255, null=True, blank=True)
    user_comment = models.TextField('Комментарий пользователя', null=True, blank=True)
    status = models.ForeignKey(OrderStatus, verbose_name='Статус заказа', on_delete=models.CASCADE, default=1)
    frontpad_id = models.IntegerField('Id в системе Frontpad', null=True, blank=True, editable=False)

    def __str__(self):
        return f"Заказ №{self.pk}"

    def get_products_price_total(self):
        """Возвращает стоимость товаров в корзине."""
        s = 0
        for p in self.cartproduct_set.all():
            s += p.price * p.count
        return s

    def get_price_total(self):
        """Возвращает стоимость заказа."""
        s = self.get_products_price_total()
        if self.delivery_mode == 'courier':
            delivery_settings, created = DeliverySettings.objects.get_or_create()
            if delivery_settings.product:
                s += delivery_settings.product.price
            else:
                s += 100
        return s

    @property
    def is_delivery_free(self):
        """Бесплатная ли доставка."""
        delivery_settings, created = DeliverySettings.objects.get_or_create()
        if self.get_products_price_total() >= delivery_settings.price_discount_from:
            return True
        return False

    def save(self, *args, **kwargs):
        created = self.pk is None
        super(Order, self).save(*args, **kwargs)
        # Отправка E-Mail с данными заказа
        if created:
            html_message = loader.render_to_string(
                'shop/email/order.html',
                {
                    'order': self
                }
            )
            emails = [self.user_email]
            send_mail(
                subject=f"Заказ №{self.pk}",
                message='',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=emails,
                fail_silently=False,
                html_message=html_message)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class DeliverySettings(models.Model):
    """Модель настроек доставки."""
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Продукт')
    price_discount_from = models.PositiveIntegerField('Сумма заказа, после которой доставка бесплатная', default=800)

    class Meta:
        verbose_name = 'Настройки доставки'
        verbose_name_plural = 'Настройки доставки'
        app_label = 'settings'
