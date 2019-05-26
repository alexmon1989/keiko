from django.db import models
from keiko.utils import SeoModel


class ContactsModel(SeoModel):
    map_code = models.TextField('Код карты (HTML)', default='')
    contacts_code = models.TextField('Код контактных данных (HTML)', default='')

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
