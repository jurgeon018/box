<<<<<<< HEAD
# Generated by Django 3.0.4 on 2020-09-15 14:07
=======
<<<<<<< HEAD
# Generated by Django 3.1.1 on 2020-09-14 09:33
=======
# Generated by Django 3.0.7 on 2020-09-14 14:44
>>>>>>> 464579cd4a6f8593eafe7679c81d1687f55a88fd
>>>>>>> b77e1374f900a7d27b55f858bad0aa0bbfac39ca

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sw_order', '0001_initial'),
<<<<<<< HEAD
        ('sw_catalog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
=======
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sw_catalog', '0001_initial'),
>>>>>>> b77e1374f900a7d27b55f858bad0aa0bbfac39ca
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False, verbose_name='Замовлено')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата створення')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата оновлення')),
                ('order', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='sw_order.order', verbose_name='Замовлення')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carts', to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
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
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='sw_cart.cart', verbose_name='Корзина')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='sw_catalog.item', verbose_name='Товар')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='sw_order.order', verbose_name='Замовлення')),
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
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favour_items', to='sw_cart.cart', verbose_name='Улюблені товари')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favour_items', to='sw_catalog.item', verbose_name='Улюблені товари')),
            ],
            options={
                'verbose_name': 'Улюблений товар',
                'verbose_name_plural': 'Улюблені товари',
            },
        ),
        migrations.CreateModel(
            name='CartItemAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0, verbose_name='Ціна')),
                ('attribute_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_catalog.itemattribute', verbose_name='Атрибут')),
                ('cart_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='sw_cart.cartitem', verbose_name='Товар в корзині')),
                ('value', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_item_attributes', to='sw_catalog.itemattributevalue', verbose_name='Значення')),
                ('values', models.ManyToManyField(blank=True, to='sw_catalog.ItemAttributeValue', verbose_name='Значення')),
            ],
            options={
                'verbose_name': 'вибраний атрибут у товара в корзині',
                'verbose_name_plural': 'вибрані атрибути у товарів в корзині',
            },
        ),
    ]
