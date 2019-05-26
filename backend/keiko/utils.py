from django.db import models


class TimeStampedModel(models.Model):
    """Абстрактный класс модели, содержащий описания полей created, modified."""
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        abstract = True


class SeoModel(models.Model):
    """Абстрактный класс модели, содержащий описания SEO-тегов."""
    meta_h1 = models.CharField('Тег h1 (мета-тег)', max_length=255, null=True, blank=True)
    meta_title = models.CharField('Title (мета-тег)', max_length=255, null=True, blank=True)
    meta_keywords = models.CharField('Keywords (мета-тег)', max_length=255, null=True, blank=True)
    meta_description = models.TextField('Description (мета-тег)', null=True, blank=True)

    class Meta:
        abstract = True
