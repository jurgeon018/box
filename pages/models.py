from django.db import models 



class Page(models.Model):
  code       = models.CharField(verbose_name=("Код"), max_length=30, blank=True, null=True, unique=True)
  meta_title = models.CharField(verbose_name=("Заголовок"), max_length=255, blank=True, null=True)
  meta_descr = models.TextField(verbose_name=("Опис"), blank=True, null=True)
  meta_key   = models.TextField(verbose_name=("Ключові слова"), blank=True, null=True)
  # url        = models.URLField(verbose_name="Урл", max_length=20, blank=True, null=True)
  url        = models.CharField(verbose_name="Урл", max_length=255, blank=True, null=True)
  
  class Meta:
    app_label = 'pages'
    verbose_name="Сторінка"
    verbose_name_plural="Сторінки"
    ordering = ['id']

  def __str__(self):
    return f'{self.code}, {self.meta_title}'


class PageFeature(models.Model):
  page  = models.ForeignKey(verbose_name=("Сторінка"), to='pages.Page', related_name="features", on_delete=models.CASCADE, blank=True, null=True)
  code  = models.CharField(verbose_name=("Код"), max_length=120, null=True, blank=True, help_text=("Код, по якому контент буде діставатися у хтмл-шаблоні"))
  name  = models.CharField(verbose_name=("Назва"), max_length=120, null=True, blank=True, help_text=("Допоміжна назва, яка буде нагадувати де на сторінці знаходиться текст"))
  value = models.TextField(verbose_name=("Текст"), null=True, blank=True, help_text=("Контент, який буде відображатися на сайті"))

  class Meta:
    app_label = 'pages'
    verbose_name="текст сторінки"
    verbose_name_plural="Текста сторінки"
    unique_together = ('page', 'code',)

  def __str__(self):
    return f'{self.page}, {self.name}'


class General(models.Model):

  class Meta:
    verbose_name="Загальна інформація на сторінках"
    verbose_name_plural="Загальна інформація на сторінках"

  def __str__(self):
    return f''

class GeneralFeature(models.Model):
  general = models.ForeignKey(verbose_name=(''), to='pages.General', blank=False, null=False, on_delete=models.CASCADE)
  class Meta:
    verbose_name="Загальна інформація на сторінках"
    verbose_name_plural="Загальна інформація на сторінках"

  def __str__(self):
    return f''


class PageImage(models.Model):
  page  = models.ForeignKey(verbose_name=("Сторінка"), to='pages.Page', related_name="images", on_delete=models.CASCADE, blank=True, null=True)
  code  = models.CharField(verbose_name=("Код"), max_length=120, null=True, blank=True, help_text=("Код, по якому картинка буде діставатися у хтмл-шаблоні"))
  name  = models.CharField(verbose_name=("Назва"), max_length=120, null=True, blank=True, help_text=("Допоміжна назва, яка буде нагадувати де знаходиться картинка"))
  value = models.ImageField(verbose_name=("Картинка"), upload_to="pages/", null=True, blank=True, help_text=("Картинка, яка буде відображатися на сайті"))

  class Meta:
    app_label = 'pages'
    verbose_name="Картинки на сторінці"
    verbose_name_plural="Картинки на сторінці"
    unique_together = ('page', 'code',)

  def __str__(self):
    return f'{self.page.code}, {self.code}'


