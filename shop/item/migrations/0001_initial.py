# Generated by Django 3.0.3 on 2020-02-13 17:08

import box.shop.item.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва валюти')),
                ('is_main', models.BooleanField(default=False, help_text='Якщо валюта головна, то відносно неї будуть конвертуватись інші валюти на сайті', verbose_name='Головна')),
            ],
            options={
                'verbose_name': 'Валюта',
                'verbose_name_plural': 'Валюти',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.TextField(blank=True, null=True, verbose_name='Мета заголовок')),
                ('meta_descr', models.TextField(blank=True, null=True, verbose_name='Мета опис')),
                ('meta_key', models.TextField(blank=True, null=True, verbose_name='Мета ключові слова')),
                ('title', models.CharField(max_length=255, verbose_name='Назва')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Артикул')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Ссилка')),
                ('thumbnail', models.ImageField(blank=True, upload_to='shop/items/thumbnails', verbose_name='Маленька картинка')),
                ('old_price', models.FloatField(blank=True, null=True, verbose_name='Стара ціна')),
                ('new_price', models.FloatField(default=1, verbose_name='Актуальна ціна')),
                ('in_stock', models.BooleanField(default=True, help_text='Мітка `Є в наявнсті` на товарі на сайті', verbose_name='Є в наявності')),
                ('is_new', models.BooleanField(default=False, help_text="Мітка 'New' на товарі на сайті", verbose_name='Новий')),
                ('is_active', models.BooleanField(default=True, help_text='Присутність товару на сайті в списку товарів', verbose_name='Активний')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Створений')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Оновлений')),
                ('order', models.IntegerField(default=10, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товари',
            },
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=box.shop.item.models.item_image_folder)),
            ],
        ),
        migrations.CreateModel(
            name='ItemReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Відгук')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name="Ім'я")),
                ('rating', models.CharField(blank=True, max_length=255, null=True, verbose_name='Оцінка')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='item.Item', verbose_name='Товар')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Відгук',
                'verbose_name_plural': 'Відгуки',
            },
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='shop/items/test_item.jpg', null=True, upload_to=box.shop.item.models.item_image_folder, verbose_name='Ссилка зображення')),
                ('alt', models.CharField(blank=True, max_length=255, null=True, verbose_name='Альт')),
                ('order', models.IntegerField(default=1, verbose_name='Порядок')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='item.Item', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Зображення товару',
                'verbose_name_plural': 'Зображення товару',
            },
        ),
        migrations.CreateModel(
            name='ItemFeatureCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Назва категорії')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='item.ItemFeatureCategory', verbose_name='Батьківська категорія')),
            ],
            options={
                'verbose_name': 'Категорія характеристики',
                'verbose_name_plural': 'Категорії характеристики',
            },
        ),
        migrations.CreateModel(
            name='ItemFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Назва характеристики')),
                ('code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Код')),
                ('value', models.TextField(blank=True, null=True, verbose_name='Значення характеристики')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='item.ItemFeatureCategory', verbose_name='Категорія характеристики')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='features', to='item.Item', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Характеристика товару',
                'verbose_name_plural': 'Характеристики товару',
            },
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.TextField(blank=True, null=True, verbose_name='Мета заголовок')),
                ('meta_descr', models.TextField(blank=True, null=True, verbose_name='Мета опис')),
                ('meta_key', models.TextField(blank=True, null=True, verbose_name='Мета ключові слова')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Посилання')),
                ('alt', models.CharField(blank=True, max_length=255, null=True, verbose_name='Альт до картинки')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Назва')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='shop/categories', verbose_name='Картинка')),
                ('is_active', models.BooleanField(default=True, help_text='Присутність категорії на сайті', verbose_name='Чи активна')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Створено')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Оновлено')),
                ('currency', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='item.Currency', verbose_name='Валюта')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='item.ItemCategory', verbose_name='Батьківська категорія')),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='item.ItemCategory', verbose_name='Категорія'),
        ),
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.ForeignKey(blank=True, help_text='Якщо залишити порожнім, то буде встановлена валюта категорії, у якій знаходиться товар', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='item.Currency', verbose_name='Валюта'),
        ),
        migrations.CreateModel(
            name='CurrencyRatio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratio', models.FloatField(help_text='Скільки одиниць порівнюваної валюти міститься в 1 одиниці головної валюти', verbose_name='Співвідношення')),
                ('compared', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratio_compared', to='item.Currency', verbose_name='Порівнювана валюта')),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratio_main', to='item.Currency', verbose_name='Головна валюта')),
            ],
            options={
                'verbose_name': 'Співвідношення валют',
                'verbose_name_plural': 'Співвідношення валют',
                'unique_together': {('main', 'compared')},
            },
        ),
    ]
