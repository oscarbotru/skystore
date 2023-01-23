from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', **NULLABLE)

    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='цена', default=0)

    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='изменен')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'{self.title}'


class Version(models.Model):
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE)
    version = models.DecimalField(decimal_places=2, max_digits=4, verbose_name='версия')
    title = models.CharField(max_length=25, verbose_name='название')

    release_date = models.DateTimeField(blank=True, null=True, verbose_name='дата релиза')

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
