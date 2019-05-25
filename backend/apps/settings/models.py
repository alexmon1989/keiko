from django.db import models
from ckeditor.fields import RichTextField


class FooterContacts(models.Model):
    """Модель настроек контактов в футере."""
    title = models.CharField('Заголовок', default='Контакты', max_length=255)
    html = RichTextField('HTML-код', blank=True)

    class Meta:
        verbose_name = 'Контакты в "футере"'
        verbose_name_plural = 'Контакты в "футере"'


class RobotsTxt(models.Model):
    """Модель для управления содержимым robots.txt"""
    content = models.TextField('Содержимое robots.txt', default='')

    class Meta:
        verbose_name = 'Содержимое robots.txt'
        verbose_name_plural = 'Содержимое robots.txt'
