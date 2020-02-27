# Generated by Django 3.0.3 on 2020-02-25 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Час')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name='Статус')),
                ('ip', models.CharField(blank=True, max_length=255, null=True, verbose_name='ІР')),
                ('amount', models.CharField(blank=True, max_length=255, null=True, verbose_name='Сумма')),
                ('currency', models.CharField(blank=True, max_length=255, null=True, verbose_name='Валюта')),
                ('sender_phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер телефону')),
                ('sender_first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Імя')),
                ('sender_last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Прізвище')),
                ('sender_card_mask2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер карти')),
                ('sender_card_bank', models.CharField(blank=True, max_length=255, null=True, verbose_name='Банк')),
                ('sender_card_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип карти')),
                ('sender_card_country', models.CharField(blank=True, max_length=255, null=True, verbose_name='Країна')),
                ('order', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.Order', verbose_name='Замовлення')),
            ],
            options={
                'verbose_name': 'Оплата',
                'verbose_name_plural': 'Оплати',
            },
        ),
    ]
