# Generated by Django 3.0 on 2020-09-07 12:06

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва купона')),
                ('discount_amount', models.FloatField(verbose_name='Знижка')),
                ('discount_type', models.CharField(choices=[('currency', 'грн.'), ('percent', '%')], default=0, max_length=255, verbose_name='Тип знижки')),
                ('requisition', models.FloatField(blank=True, help_text='Мінімальна сума, на яку потрібно зробити замовлення, щоб купон набув дійсності.', null=True, verbose_name='Умови')),
                ('period', models.DateTimeField(blank=True, null=True, verbose_name='Термін дії')),
                ('one_time', models.BooleanField(default=False, verbose_name='Одноразовий')),
                ('uses_amount', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='К-сть використань')),
            ],
            options={
                'verbose_name': 'купон',
                'verbose_name_plural': 'Список купонів',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'підписник',
                'verbose_name_plural': 'Підписники',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
            ],
            options={
                'verbose_name': 'покупець',
                'verbose_name_plural': 'Список покупців',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('project.projectuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sw_customer.Coupon', verbose_name='Купон')),
            ],
            options={
                'verbose_name': 'група',
                'verbose_name_plural': 'Групи покупців',
            },
        ),
    ]