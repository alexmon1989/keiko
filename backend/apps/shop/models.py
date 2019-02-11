from django.shortcuts import reverse
from django.db import models
from keiko.utils import TimeStampedModel


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

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Product(TimeStampedModel):
    """Модель продукта."""
    title = models.CharField('Название', max_length=255)
    image = models.ImageField('Изображение', null=True, blank=True, help_text='Размер: 450px * 450px')
    categories = models.ManyToManyField(Category, verbose_name='Категории', blank=True)
    properties = models.ManyToManyField(Property, verbose_name='Свойства', blank=True)
    ingredients = models.ManyToManyField(Ingredient, verbose_name='Ингредиенты', blank=True)
    price = models.FloatField('Цена', blank=True, null=True)
    frontpad_id = models.PositiveIntegerField('id товара в системе Frontpad', null=True, blank=True)
    is_enabled = models.BooleanField('Включено', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
