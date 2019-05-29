from django.db import models
from ckeditor.fields import RichTextField
from keiko.utils import SeoModel


class ContactsModel(SeoModel):
    map_code = models.TextField('Код карты (HTML)', default='')
    contacts_code = RichTextField('Контактные данные', default='')

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
