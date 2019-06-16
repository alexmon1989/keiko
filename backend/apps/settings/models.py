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


class SocialUrl(models.Model):
    """Модель для управления ссылками на социальные сети."""
    social_network_title = models.CharField('Название социальной сети', max_length=255)
    url = models.URLField('Ссылка')
    icon_class = models.CharField('CSS-класс иконки', max_length=255, blank=True, default='')
    weight = models.IntegerField(
        'Вес', default=1000, help_text='Чем выше вес, тем левее элемент в списке ссылок на соц. сети.')
    is_enabled = models.BooleanField('Включено', default=True)

    def __str__(self):
        return self.social_network_title

    class Meta:
        verbose_name = 'Ссылка на социальную сеть'
        verbose_name_plural = 'Ссылки на социальные сети'


class HeaderPhone(models.Model):
    """Модель для управления значением номера телефона в шапке сайта."""
    value = models.CharField('Значение', default='', max_length=255)

    class Meta:
        verbose_name = 'Номер телефона в шапке'
        verbose_name_plural = 'Номер телефона в шапке'


class Analytics(models.Model):
    """Модель для управления кодом аналитики."""
    code = models.TextField('Код аналитики', default='')

    class Meta:
        verbose_name = 'HTML-код аналитики'
        verbose_name_plural = 'HTML-код аналитики'
