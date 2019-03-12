from django.db import models
from ckeditor.fields import RichTextField


class FooterContacts(models.Model):
    """Модель настроек контактов в футере."""
    title = models.CharField('Заголовок', default='Контакты', max_length=255)
    html = RichTextField('HTML-код', blank=True)

    class Meta:
        verbose_name = 'Контакты в "футере"'
        verbose_name_plural = 'Контакты в "футере"'
