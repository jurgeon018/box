# Generated by Django 3.0.7 on 2020-09-14 14:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LiqpayConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liqpay_public_key', models.TextField(default='i46942964050', verbose_name='Публічний ключ')),
                ('liqpay_private_key', models.TextField(default='e0EMc79BGqm2oieTc4ujvq2iv7NPjNu7MmSlEAoM', verbose_name='Приватний ключ')),
                ('liqpay_sandbox_public_key', models.TextField(default='sandbox_i36382218041', verbose_name='Тестовий публічний ключ')),
                ('liqpay_sandbox_private_key', models.TextField(default='sandbox_XcBJpBTSMHJqN9Ms1mYtYEd7Ha7oW9LlDz8YZQcr', verbose_name='Тестовий приватний ключ')),
                ('sandbox_mode', models.BooleanField(default=True, verbose_name='Тестовий режим')),
            ],
            options={
                'verbose_name': 'налаштування Liqpay',
                'verbose_name_plural': 'налаштування Liqpay',
            },
        ),
        migrations.CreateModel(
            name='LiqpayTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Час')),
                ('action', models.CharField(blank=True, max_length=255, null=True, verbose_name='action')),
                ('payment_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='payment_id')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name='status')),
                ('version', models.CharField(blank=True, max_length=255, null=True, verbose_name='version')),
                ('type', models.CharField(blank=True, max_length=255, null=True, verbose_name='type')),
                ('paytype', models.CharField(blank=True, max_length=255, null=True, verbose_name='paytype')),
                ('public_key', models.CharField(blank=True, max_length=255, null=True, verbose_name='public_key')),
                ('acq_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='acq_id')),
                ('order_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='order_id')),
                ('liqpay_order_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='liqpay_order_id')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='description')),
                ('sender_phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='sender_phone')),
                ('sender_first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='sender_first_name')),
                ('sender_last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='sender_last_name')),
                ('sender_card_mask2', models.CharField(blank=True, max_length=255, null=True, verbose_name='sender_card_mask2')),
                ('sender_card_bank', models.CharField(blank=True, max_length=255, null=True, verbose_name='sender_card_bank')),
                ('sender_card_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='sender_card_type')),
                ('sender_card_country', models.CharField(blank=True, max_length=255, null=True, verbose_name='sender_card_country')),
                ('ip', models.CharField(blank=True, max_length=255, null=True, verbose_name='ip')),
                ('amount', models.CharField(blank=True, max_length=255, null=True, verbose_name='amount')),
                ('currency', models.CharField(blank=True, max_length=255, null=True, verbose_name='currency')),
                ('sender_commission', models.CharField(blank=True, max_length=255, null=True, verbose_name='sender_commission')),
                ('receiver_commission', models.CharField(blank=True, max_length=255, null=True, verbose_name='receiver_commission')),
                ('agent_commission', models.CharField(blank=True, max_length=255, null=True, verbose_name='agent_commission')),
                ('amount_debit', models.CharField(blank=True, max_length=255, null=True, verbose_name='amount_debit')),
                ('amount_credit', models.CharField(blank=True, max_length=255, null=True, verbose_name='amount_credit')),
                ('commission_debit', models.CharField(blank=True, max_length=255, null=True, verbose_name='commission_debit')),
                ('commission_credit', models.CharField(blank=True, max_length=255, null=True, verbose_name='commission_credit')),
                ('currency_debit', models.CharField(blank=True, max_length=255, null=True, verbose_name='currency_debit')),
                ('currency_credit', models.CharField(blank=True, max_length=255, null=True, verbose_name='currency_credit')),
                ('sender_bonus', models.CharField(blank=True, max_length=255, null=True, verbose_name='sender_bonus')),
                ('amount_bonus', models.CharField(blank=True, max_length=255, null=True, verbose_name='amount_bonus')),
                ('mpi_eci', models.CharField(blank=True, max_length=255, null=True, verbose_name='mpi_eci')),
                ('is_3ds', models.CharField(blank=True, max_length=255, null=True, verbose_name='is_3ds')),
                ('language', models.CharField(blank=True, max_length=255, null=True, verbose_name='language')),
                ('create_date', models.CharField(blank=True, max_length=255, null=True, verbose_name='create_date')),
                ('end_date', models.CharField(blank=True, max_length=255, null=True, verbose_name='end_date')),
                ('transaction_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='transaction_id')),
            ],
            options={
                'verbose_name': 'трансзакція liqpay',
                'verbose_name_plural': 'трансзакції liqpay',
            },
        ),
    ]
