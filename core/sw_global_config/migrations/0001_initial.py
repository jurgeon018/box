# Generated by Django 3.0 on 2020-09-07 12:06

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('robots', models.CharField(blank=True, choices=[('index, nofollow', 'index, nofollow'), ('index, follow', 'index, follow'), ('noindex, nofollow', 'noindex, nofollow'), ('noindex, follow', 'noindex, follow')], default=None, max_length=255, null=True, verbose_name='Meta Robots')),
                ('robots_txt', models.TextField(blank=True, null=True, verbose_name='robots.txt')),
                ('favicon', models.ImageField(blank=True, default='favicon/favicon.ico', help_text='Допустимі розширення зображень png, gif, jpg, jpeg, ico', null=True, upload_to='favicon', verbose_name='Фавікон сайту')),
                ('og_image_square', models.ImageField(blank=True, default='ogimage/square.png', null=True, upload_to='ogimage', verbose_name='og:image квадрат')),
                ('og_image_square_uk', models.ImageField(blank=True, default='ogimage/square.png', null=True, upload_to='ogimage', verbose_name='og:image квадрат')),
                ('og_image_square_en', models.ImageField(blank=True, default='ogimage/square.png', null=True, upload_to='ogimage', verbose_name='og:image квадрат')),
                ('og_image_square_ru', models.ImageField(blank=True, default='ogimage/square.png', null=True, upload_to='ogimage', verbose_name='og:image квадрат')),
                ('og_image_rectangle', models.ImageField(blank=True, default='ogimage/rectangle.png', null=True, upload_to='ogimage', verbose_name='og:image прямокутник')),
                ('og_image_rectangle_uk', models.ImageField(blank=True, default='ogimage/rectangle.png', null=True, upload_to='ogimage', verbose_name='og:image прямокутник')),
                ('og_image_rectangle_en', models.ImageField(blank=True, default='ogimage/rectangle.png', null=True, upload_to='ogimage', verbose_name='og:image прямокутник')),
                ('og_image_rectangle_ru', models.ImageField(blank=True, default='ogimage/rectangle.png', null=True, upload_to='ogimage', verbose_name='og:image прямокутник')),
                ('host', models.CharField(blank=True, default='mail.starwayua.com', help_text='Сервер', max_length=256, null=True, verbose_name='EMAIL_HOST')),
                ('port', models.SmallIntegerField(blank=True, default=587, help_text='Порт', null=True, verbose_name='EMAIL_PORT')),
                ('from_email', models.CharField(blank=True, default='dev@starwayua.com', help_text='Почта відправки листів', max_length=256, null=True, verbose_name='DEFAULT_FROM_EMAIL')),
                ('username', models.CharField(blank=True, default='dev@starwayua.com', help_text='Логін', max_length=256, null=True, verbose_name='EMAIL_HOST_USER')),
                ('password', models.CharField(blank=True, default='dev69018', help_text='Пароль', max_length=256, null=True, verbose_name='EMAIL_HOST_PASSWORD')),
                ('use_tls', models.BooleanField(default=True, help_text=' ', verbose_name='EMAIL_USE_TLS')),
                ('use_ssl', models.BooleanField(default=False, help_text=' ', verbose_name='EMAIL_USE_SSL')),
                ('fail_silently', models.BooleanField(default=False, help_text='Помилка при невдалій відправці', verbose_name='fail_silently')),
                ('timeout', models.SmallIntegerField(blank=True, help_text='Таймаут в секундах', null=True, verbose_name='timeout')),
            ],
            options={
                'verbose_name': 'Глобальні налаштування',
                'verbose_name_plural': 'Глобальні налаштування',
            },
        ),
        migrations.CreateModel(
            name='GlobalLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Текст')),
                ('text_uk', models.CharField(max_length=255, null=True, verbose_name='Текст')),
                ('text_en', models.CharField(max_length=255, null=True, verbose_name='Текст')),
                ('text_ru', models.CharField(max_length=255, null=True, verbose_name='Текст')),
                ('code', models.SlugField(blank=True, null=True, unique=True, verbose_name='Код')),
            ],
            options={
                'verbose_name': 'мітка',
                'verbose_name_plural': 'мітки',
            },
        ),
        migrations.CreateModel(
            name='GlobalMarker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
                ('name_uk', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('code', models.SlugField(blank=True, null=True, unique=True, verbose_name='Код')),
            ],
            options={
                'verbose_name': 'маркер',
                'verbose_name_plural': 'маркери',
            },
        ),
        migrations.CreateModel(
            name='SeoScript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(verbose_name='Код для вставлення')),
                ('name', models.CharField(max_length=255, verbose_name='Назва коду')),
                ('position', models.CharField(choices=[('head_top', 'Після відкриваючого head'), ('body_top', 'Після відкриваючого body'), ('head_bottom', 'Перед закриваючим head'), ('body_bottom', 'Перед закриваючим body')], max_length=255, verbose_name='Положення коду на сторінці')),
                ('setting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scripts', to='sw_global_config.GlobalConfig')),
            ],
            options={
                'verbose_name': 'Код',
                'verbose_name_plural': 'Коди',
            },
        ),
        migrations.CreateModel(
            name='GlobalTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18, verbose_name='Колір')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
                ('name_uk', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('config', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sw_global_config.GlobalConfig', verbose_name='Глобальні налаштування')),
            ],
            options={
                'verbose_name': 'тег',
                'verbose_name_plural': 'теги',
            },
        ),
        migrations.CreateModel(
            name='GlobalRecipientEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, verbose_name='Емайл')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активність')),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='sw_global_config.GlobalConfig', verbose_name='Глобальні налаштування')),
            ],
            options={
                'verbose_name': 'емейл для всіх сповіщень',
                'verbose_name_plural': 'емейли для всіх сповіщень',
            },
        ),
    ]
