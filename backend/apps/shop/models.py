from django.db import models
from keiko.utils import TimeStampedModel


class Category(TimeStampedModel):
    """Модель категории продукта."""
    title = models.CharField('Название', max_length=255)
    weight = models.IntegerField('Вес', default=1000, help_text='Чем выше вес, тем выше элемент в списке категорий.')
    is_enabled = models.BooleanField('Включено', default=True)

    def __str__(self):
        return self.title

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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Product(TimeStampedModel):
    """Модель продукта."""
    title = models.CharField('Название', max_length=255)
    categories = models.ManyToManyField(Category, verbose_name='Категории')
    properties = models.ManyToManyField(Property, verbose_name='Свойства')
    ingredients = models.ManyToManyField(Ingredient, verbose_name='Ингредиенты')
    price = models.FloatField('Цена', blank=True, null=True)
    frontpad_id = models.PositiveIntegerField('id товара в системе Frontpad', null=True, blank=True)
    is_enabled = models.BooleanField('Включено', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
