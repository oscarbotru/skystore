# Generated by Django 4.1.5 on 2023-01-23 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='версия')),
                ('title', models.CharField(max_length=25, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('release_date', models.DateTimeField(blank=True, null=True, verbose_name='дата релиза')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]