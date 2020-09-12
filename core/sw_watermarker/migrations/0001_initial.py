# Generated by Django 3.0 on 2020-09-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Watermark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('image', models.ImageField(upload_to='watermarks', verbose_name='image')),
                ('is_active', models.BooleanField(blank=True, default=True, verbose_name='is active')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'watermark',
                'verbose_name_plural': 'watermarks',
                'ordering': ['name'],
            },
        ),
    ]