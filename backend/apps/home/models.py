from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from keiko.utils import TimeStampedModel, SeoModel


class Slide(TimeStampedModel):
    """Модель слайда."""
    title = models.CharField('Заголовок', max_length=255, null=True, blank=True)
    link = models.URLField('Ссылка', null=True, blank=True)
    text = RichTextField('Текст', null=True, blank=True)
    image = models.ImageField('Изображение', help_text='Размер: 1920px * 1080px')
    weight = models.IntegerField('Вес', default=1000, help_text='Чем выше вес, тем выше элемент в списке категорий.')
    is_enabled = models.BooleanField('Включено', default=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайдер'


class Page(SeoModel):
    content = RichTextUploadingField('Текст', default='', blank=True, null=True)

    class Meta:
        verbose_name = 'Данные страницы'
        verbose_name_plural = 'Данные страницы'
