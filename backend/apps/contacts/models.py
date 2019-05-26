from django.db import models


class ContactsModel(models.Model):
    map_code = models.TextField('Код карты (HTML)', default='')
    contacts_code = models.TextField('Код контактных данных (HTML)', default='')

    class Meta:
        verbose_name = 'Контаты'
        verbose_name_plural = 'Контаты'
