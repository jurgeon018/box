from django.db import models 


class FeatureValue(models.Model):
    value = models.CharField(verbose_name="Значення", max_length=255)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'значення характеристики'
        verbose_name_plural = 'значення характеристик'


class Feature(models.Model):
    name = models.CharField(verbose_name="Назва", max_length=255)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'назва характеристики'
        verbose_name_plural = 'назви характеристик'


class ItemFeature(models.Model):
    # items = models.ManyToManyField(to="sw_catalog.Item", verbose_name="Товари")
    item  = models.ForeignKey(to="sw_catalog.Item", verbose_name="Товар", on_delete=models.CASCADE)
    name  = models.ForeignKey(to="sw_catalog.Feature", verbose_name="Назва характеристики", on_delete=models.CASCADE)
    value = models.ForeignKey(to="sw_catalog.FeatureValue", verbose_name="Значення характеристики", on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name="Активність", default=True)
    code      = models.SlugField(verbose_name='Код', blank=True, null=True, unique=True)

    def __str__(self):
        return f'{self.name}:{self.value} - {self.item}'

    class Meta:
        verbose_name = 'характеристика товара'
        verbose_name_plural = 'характеристики товара'





