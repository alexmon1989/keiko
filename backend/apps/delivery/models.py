from ckeditor_uploader.fields import RichTextUploadingField
from keiko.utils import SeoModel, TimeStampedModel


class Page(SeoModel, TimeStampedModel):
    """Модель содержимого страницы доставки."""
    content = RichTextUploadingField(
        'Текст на странице',
        default='',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Данные страницы'
        verbose_name_plural = 'Данные страницы'
