# Generated by Django 2.0 on 2020-02-11 14:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False, verbose_name='Замовлено')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата створення')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата оновлення')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзини',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False, verbose_name='Замовлено')),
                ('quantity', models.IntegerField(default=1, verbose_name='Кількість')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Товар в корзині',
                'verbose_name_plural': 'Товари в корзині',
            },
        ),
        migrations.CreateModel(
            name='FavourItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favour_items', to='cart.Cart', verbose_name='Улюблені товари')),
            ],
            options={
                'verbose_name': 'Улюблений товар',
                'verbose_name_plural': 'Улюблені товари',
            },
        ),
    ]
