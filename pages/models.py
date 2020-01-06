from django.db import models 
from tinymce.models import HTMLField
from django.shortcuts import reverse


class Page(models.Model):
  code       = models.CharField(max_length=30, blank=True, null=True, unique=True)
  meta_title = models.TextField(blank=True, null=True)
  meta_descr = models.TextField(blank=True, null=True)
  meta_key   = models.TextField(blank=True, null=True)
  # url        = models.URLField(verbose_name="Урл", max_length=20, blank=True, null=True)

  class Meta:
    app_label = 'pages'
    verbose_name="мета інформація до сторінки"
    verbose_name_plural="Мета інформація до сторінок"

  def __str__(self):
    return f'{self.meta_title}'


class PageFeature(models.Model):
  page  = models.ForeignKey(verbose_name=("Сторінка"), to='Page', related_name="features", on_delete=models.CASCADE, blank=True, null=True)
  code  = models.CharField(verbose_name=("Код"), max_length=120, null=True, blank=True, help_text=("Код, по якому контент буде діставатися у хтмл-шаблоні"))
  name  = models.CharField(verbose_name=("Назва"), max_length=120, null=True, blank=True, help_text=("Допоміжна назва"))
  value = models.TextField(verbose_name=("Текст"), null=True, blank=True, help_text=("Контент, який буде відображатися на сайті"))

  class Meta:
    app_label = 'pages'
    verbose_name="текст сторінки"
    verbose_name_plural="Текста сторінки"
    unique_together = ('page', 'code',)

  def __str__(self):
    return f'{self.page}, {self.name}'



class PageImage(models.Model):
  page  = models.ForeignKey(verbose_name=("Сторінка"), to='Page', related_name="images", on_delete=models.CASCADE, blank=True, null=True)
  code  = models.CharField(verbose_name=("Код"), max_length=120, null=True, blank=True, help_text=("Код, по якому картинка буде діставатися у хтмл-шаблоні"))
  name  = models.CharField(verbose_name=("Назва"), max_length=120, null=True, blank=True, help_text=("Допоміжна описувальна назва"))
  value = models.ImageField(verbose_name=("Картинка"), upload_to="pages/", null=True, blank=True, help_text=("Картинка, яка буде відображатися на сайті"))

  class Meta:
    app_label = 'pages'
    verbose_name="Картинки на сторінці"
    verbose_name_plural="Картинки на сторінці"
    unique_together = ('page', 'code',)

  def __str__(self):
    return f'{self.page.code}, {self.code}'



class Slider(models.Model):
  page  = models.ForeignKey(to="Page", related_name="sliders", on_delete=models.CASCADE, blank=True, null=True)
  title = models.TextField(verbose_name=("Заголовок"), blank=True, null=True)
  text  = models.TextField(verbose_name=("Текст"), blank=True, null=True)
  # image = models.ImageField(verbose_name=("Картинка"), blank=True, null=True)
  # alt   = models.CharField(verbose_name=("Альт-картинки"), max_length=120, blank=True, null=True)
  video = models.FileField(verbose_name=("Відео"), blank=True, null=True, upload_to="sliders/")
  btn   = models.BooleanField(verbose_name=("Кнопка 'Більше'"), default=True, help_text=("Кнопка 'показати більше', яка веде на категорію товарів"))
  link  = models.URLField(verbose_name=("Ссилка"), blank=True, null=True)
  category = models.ForeignKey(verbose_name=("Категорія"), to=("item.ItemCategory"), related_name='sliders', on_delete=models.CASCADE, blank=True, null=True)

  class Meta:
    verbose_name="Слайдер на головній"
    verbose_name_plural="Слайдери на головній"

  def __str__(self):
    return f'{self.page}'


class Icon(models.Model):
  page  = models.ForeignKey(verbose_name=("Сторінка"), to="pages.Page", on_delete=models.CASCADE, related_name='icons')
  title = models.TextField( verbose_name=("Заголовок"), )
  text  = models.TextField( verbose_name=("Текст"), )
  
  class Meta:
    verbose_name="Іконка на головній"
    verbose_name_plural="Іконки на головній"

  def __str__(self):
    return f'{self.page}'


class Team(models.Model):
  page     = models.ForeignKey(verbose_name=("Сторінка"), to="pages.Page", on_delete=models.SET_NULL, related_name='team', blank=True, null=True)
  name     = models.TextField(verbose_name=("Ім'я"), blank=True, null=True)
  position = models.TextField(verbose_name=("Посада"), blank=True, null=True) 
  image    = models.ImageField(verbose_name=("Фото"), upload_to='about/')
  alt      = models.CharField(max_length=255, blank=True, null=True, help_text='Альтернативний надпис до фотки, потрібен для SEO.')
  
  class Meta:
    verbose_name="Команда"
    verbose_name_plural="Команда"

  def __str__(self):
    return f'{self.name}, {self.position}'




