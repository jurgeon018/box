<<<<<<< HEAD
# Generated by Django 3.1.1 on 2020-09-14 09:33
=======
# Generated by Django 3.0.7 on 2020-09-14 14:44
>>>>>>> 464579cd4a6f8593eafe7679c81d1687f55a88fd

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Імя')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Примітки адміністратора')),
                ('url', models.CharField(blank=True, help_text='Ссилка на сторінку, з якої було відправлено контактну форму', max_length=255, null=True, verbose_name='Ссилка')),
                ('checked', models.BooleanField(default=False, verbose_name='Оброблено')),
            ],
            options={
                'verbose_name': 'Зворотний звязок',
                'verbose_name_plural': 'Зворотний звязок',
            },
        ),
        migrations.CreateModel(
            name='ContactConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Налаштування зворотнього звязку',
                'verbose_name_plural': 'Налаштування зворотнього звязку',
            },
        ),
        migrations.CreateModel(
            name='ContactRecipientEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, verbose_name='Емайл')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активність')),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='sw_contact_form.contactconfig')),
            ],
            options={
                'verbose_name': 'емейл для сповіщень про контактні форми',
                'verbose_name_plural': 'емейли для сповіщень про контактні форми',
            },
        ),
    ]
