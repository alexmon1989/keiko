from django.db import models
from django.shortcuts import reverse
from keiko.utils import SeoModel, TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


class PromotionArticle(SeoModel, TimeStampedModel):
    """Модель акции (статьи)."""
    title = models.CharField('Заголовок', max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField('Изображение', null=True, blank=True, help_text='Размер: 450px * 450px')
    short_text = RichTextField(
        'Короткий текст',
        blank=True,
        null=True,
        help_text='Отображается на странице со списком акций'
    )
    full_text = RichTextUploadingField(
        'Полный текст',
        blank=True,
        null=True,
        help_text='Отображается на странице акции'
    )
    is_enabled = models.BooleanField('Включено', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('promotions:detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
