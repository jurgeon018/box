# Generated by Django 3.0.7 on 2020-09-14 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Title')),
                ('title_uk', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Title')),
                ('title_en', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Область',
                'verbose_name_plural': 'Області',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Title')),
                ('title_uk', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Title')),
                ('title_en', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Title')),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sw_novaposhta.Area', verbose_name='Area')),
            ],
            options={
                'verbose_name': 'район',
                'verbose_name_plural': 'райони',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Title')),
                ('title_uk', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Title')),
                ('title_en', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Тип населеного пункту',
                'verbose_name_plural': 'Типи населених пунктів',
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Title')),
                ('title_uk', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Title')),
                ('title_en', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Title')),
                ('address', models.CharField(db_index=True, max_length=255, verbose_name='Address')),
                ('address_uk', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Address')),
                ('address_en', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Address')),
                ('address_ru', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Address')),
            ],
            options={
                'verbose_name': 'Warehouse',
                'verbose_name_plural': 'Warehouses',
            },
        ),
        migrations.CreateModel(
            name='Settlement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Title')),
                ('title_uk', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Title')),
                ('title_en', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Title')),
                ('latitude', models.CharField(max_length=255, verbose_name='latitude')),
                ('longitude', models.CharField(max_length=255, verbose_name='longitude')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sw_novaposhta.Region', verbose_name='Region')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sw_novaposhta.Type', verbose_name='Type')),
                ('type_en', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sw_novaposhta.Type', verbose_name='Type')),
                ('type_ru', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sw_novaposhta.Type', verbose_name='Type')),
                ('type_uk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sw_novaposhta.Type', verbose_name='Type')),
            ],
            options={
                'verbose_name': 'населений пункт',
                'verbose_name_plural': 'населені пункти',
            },
        ),
    ]
