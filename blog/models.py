from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.SlugField(verbose_name='slug', blank=True, null=True)
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='изображение')

    is_published = models.BooleanField(default=False, verbose_name='опубликовано')
    views = models.PositiveIntegerField(default=0, verbose_name='просмотры')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    def __str__(self):
        return f'{self.title}'
