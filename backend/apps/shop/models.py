from django.shortcuts import reverse
from django.db import models
from keiko.utils import TimeStampedModel
from ckeditor.fields import RichTextField
import json


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
