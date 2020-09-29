# Generated by Django 3.1.1 on 2020-09-15 10:16

import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sw_global_config', '0001_initial'),
        ('sw_customer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sw_currency', '0001_initial'),
        ('sw_catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField(default=0, verbose_name='Сумма замовлення')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Імя')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Е-майл')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер телефона')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Коментарии')),
                ('payment_opt', models.CharField(blank=True, max_length=255, null=True, verbose_name='Спосіб оплати')),
                ('delivery_opt', models.CharField(blank=True, max_length=255, null=True, verbose_name='Спосіб доставки')),
                ('ordered', models.BooleanField(default=False, verbose_name='Завершено')),
                ('paid', models.BooleanField(default=False, verbose_name='Сплачено')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Примітки адміністратора')),
                ('is_active', models.BooleanField(default=True, help_text='Замість видалення замовлення потрібно виключити це поле', verbose_name='Активність')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата замовлення')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата оновлення')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sw_customer.coupon', verbose_name='Купон')),
            ],
            options={
                'verbose_name': 'замовлення',
                'verbose_name_plural': 'замовлення',
            },
        ),
        migrations.CreateModel(
            name='OrderConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Налаштування замовленя',
                'verbose_name_plural': 'Налаштування замовленя',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, default=0, null=True, verbose_name='Сумма')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='створено')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='оновлено')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sw_currency.currency', verbose_name='Валюта')),
                ('order', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sw_order.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'оплата замовлення',
                'verbose_name_plural': 'оплати замовлень',
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18, verbose_name='Колір')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
                ('name_uk', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('config', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sw_order.orderconfig')),
            ],
            options={
                'verbose_name': 'статус замовленнь',
                'verbose_name_plural': 'cтатуси замовленнь',
            },
        ),
        migrations.CreateModel(
            name='OrderRecipientEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, verbose_name='Емайл')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активність')),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='sw_order.orderconfig', verbose_name='Налаштування')),
            ],
            options={
                'verbose_name': 'емейл для сповіщень про замовлення',
                'verbose_name_plural': 'емейли для сповіщень про замовлення',
            },
        ),
        migrations.CreateModel(
            name='OrderAdditionalPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Ціна')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='sw_order.orderconfig', verbose_name='Налаштування')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_currency.currency', verbose_name='Валюта')),
            ],
            options={
                'verbose_name': 'емейл для сповіщень про замовлення',
                'verbose_name_plural': 'емейли для сповіщень про замовлення',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sw_order.orderstatus', verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='order',
            name='tags',
            field=models.ManyToManyField(blank=True, to='sw_global_config.GlobalTag', verbose_name='Мітки'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Користувач'),
        ),
        migrations.CreateModel(
            name='ItemRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name="Ім'я")),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Емайл')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Повідомлення')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Створено')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sw_catalog.item', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Заявка на інформацію про товар',
                'verbose_name_plural': 'Заявки на інформацію про товар',
            },
        ),
    ]
