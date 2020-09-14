# Generated by Django 3.0.7 on 2020-09-07 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        # ('liqpay', '0002_auto_20200826_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liqpayconfig',
            name='liqpay_private_key',
            field=models.TextField(default='e0EMc79BGqm2oieTc4ujvq2iv7NPjNu7MmSlEAoM', verbose_name='Приватний ключ'),
        ),
        migrations.AlterField(
            model_name='liqpayconfig',
            name='liqpay_public_key',
            field=models.TextField(default='i46942964050', verbose_name='Публічний ключ'),
        ),
        migrations.AlterField(
            model_name='liqpayconfig',
            name='liqpay_sandbox_private_key',
            field=models.TextField(default='sandbox_XcBJpBTSMHJqN9Ms1mYtYEd7Ha7oW9LlDz8YZQcr', verbose_name='Тестовий приватний ключ'),
        ),
        migrations.AlterField(
            model_name='liqpayconfig',
            name='liqpay_sandbox_public_key',
            field=models.TextField(default='sandbox_i36382218041', verbose_name='Тестовий публічний ключ'),
        ),
    ]