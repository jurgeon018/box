# Generated by Django 3.0.7 on 2020-07-03 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(help_text='Наприклад: грн., дол., $, руб., Є. Буде відображатись біля ціни в товарі.', max_length=255, verbose_name='Символ')),
                ('symbol_uk', models.CharField(help_text='Наприклад: грн., дол., $, руб., Є. Буде відображатись біля ціни в товарі.', max_length=255, null=True, verbose_name='Символ')),
                ('symbol_en', models.CharField(help_text='Наприклад: грн., дол., $, руб., Є. Буде відображатись біля ціни в товарі.', max_length=255, null=True, verbose_name='Символ')),
                ('symbol_ru', models.CharField(help_text='Наприклад: грн., дол., $, руб., Є. Буде відображатись біля ціни в товарі.', max_length=255, null=True, verbose_name='Символ')),
                ('code', models.SlugField(max_length=255, unique=True, verbose_name='Код ІSO')),
                ('sale_rate', models.FloatField(null=True, verbose_name='Курс продажі')),
                ('purchase_rate', models.FloatField(null=True, verbose_name='Курс купівлі')),
                ('is_main', models.BooleanField(default=False, verbose_name='Головна')),
            ],
            options={
                'verbose_name': 'валюта',
                'verbose_name_plural': 'валюти',
            },
        ),
        migrations.CreateModel(
            name='CurrencyConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_field', models.CharField(choices=[('purchase', 'по курсу купівлі'), ('sale', 'по курсу продажі')], default='purchase', max_length=255, verbose_name='Поле для конвертації')),
            ],
            options={
                'verbose_name': 'Налаштування валют',
                'verbose_name_plural': 'Налаштування валют',
            },
        ),
        migrations.CreateModel(
            name='ParseCurrency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('UAH', 'UAH'), ('RUB', 'RUB'), ('EUR', 'EUR'), ('USD', 'USD'), ('AZN', 'AZN'), ('BYN', 'BYN'), ('CAD', 'CAD'), ('CHF', 'CHF'), ('CZK', 'CZK'), ('UZS', 'UZS')], max_length=255, unique=True, verbose_name='Назва')),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_currency.CurrencyConfig')),
            ],
            options={
                'verbose_name': 'Валюта для парсингу',
                'verbose_name_plural': 'Валюти для парсингу',
                'unique_together': {('name', 'config')},
            },
        ),
    ]
