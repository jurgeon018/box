from django.core.files import File
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.utils import timezone 
from django.db import models
# from django.utils.safestring import mark_safe
from django.utils.html import mark_safe
from django.core.files.base import ContentFile
from django.conf import settings 
from django.utils.text import slugify
from transliterate import translit, get_available_language_codes
from django.utils.text import slugify
# from transliterate import slugify

from transliterate import translit
import os 
from PIL import Image

from box.shop.item import settings as item_settings 
from .managers import * 

from mptt.models import MPTTModel, TreeForeignKey


__all__ = [
	"ItemCurrency",
	"ItemCurrencyRatio",
	"ItemStock",
	"ItemMarker",
	"ItemManufacturer",
	"Item",
	"ItemCategory",
	"ItemBrand",
	"ItemImage",
	"ItemFeatureName",
	"ItemFeature",
	"ItemFeatureCategory",
	"ItemReview",
]


User = get_user_model()


STOCK_COLOR_CHOICES = (
	('g', "green"),
	('o', "orange"),
	('r', "red"),
)


class ItemCurrency(models.Model):
	# TODO: 
	# Валюти як на mottoex.com.ua, чи валюти як на serwis-kop.pl? 
	# Вибір в settings.py
	name      = models.CharField(verbose_name=("Назва"), max_length=255)
	symbol    = models.CharField(verbose_name=("Знак"), max_length=255)
	code      = models.CharField(verbose_name=("Код ІSO"), max_length=255)
	rate      = models.DecimalField(verbose_name=("Курс"), max_digits=9, decimal_places=7, blank=False, null=True)
	is_active = models.BooleanField(verbose_name=("Активність"), default=True)
	is_main   = models.BooleanField(
		verbose_name=("Головна"), 
		default=False, 
		help_text=("Якщо валюта головна, то відносно неї будуть конвертуватись інші валюти на сайті")
		# help_text=("Основной валютой сайта считается та, которая стоит первой в списке. Для того чтобы сменить основную валюту, просто перетяните нужную вам валюту на первое место ")
	)

	class Meta: 
		verbose_name = ('Валюта'); 
		verbose_name_plural = ('Валюти')

	def __str__(self):
		return f"{self.name}"
	@classmethod
	def modeltranslation_fields(cls):
		fields = [
		    'name',
			'symbol',
		]
		return fields

	def save(self, *args, **kwargs):
		ItemCurrency.objects.all().update(is_main=False)
		super().save(*args, **kwargs)


class ItemCurrencyRatio(models.Model):
	main     = models.ForeignKey(verbose_name=("Головна валюта"),     to="item.ItemCurrency", on_delete=models.CASCADE, related_name="ratio_main")
	compared = models.ForeignKey(verbose_name=("Порівнювана валюта"), to="item.ItemCurrency", on_delete=models.CASCADE, related_name="ratio_compared")
	ratio    = models.FloatField(verbose_name=("Співвідношення"), help_text=(f"Скільки одиниць порівнюваної валюти міститься в 1 одиниці головної валюти"))

	class Meta: 
		verbose_name = ('Співвідношення валют'); 
		verbose_name_plural = ('Співвідношення валют')
		unique_together = ('main','compared')

	def __str__(self):
		return f"{self.main}, {self.compared}"


from django.db.models.signals import pre_save



# def pre_save_item_slug(sender, instance, *args, **kwargs):
# 	if not instance.slug:
# 		slug = slugify(translit(instance.name, reversed=True))
# 		instance.slug = slug


# pre_save.connect(pre_save_item_slug, sender=Category)


class ItemStock(models.Model):
	# code = models.NullBooleanField(verbose_name=("Код"))
	text         = models.CharField(verbose_name=('Наявність'), max_length=255, unique=True)
	availability = models.BooleanField(verbose_name=('Можливість покупки'), default=True)
	colour       = models.CharField(verbose_name=('Колір'), choices=STOCK_COLOR_CHOICES, max_length=255, default=1)
	def __str__(self):
		return f"{self.text}"
	
	class Meta:
		verbose_name = ('Статус наявності')
		verbose_name_plural = ('Статуси наявності')

	@classmethod
	def modeltranslation_fields(cls):
		fields = [
		    'text',
		]
		return fields


class ItemMarker(models.Model):
	code  = models.CharField(verbose_name=("Код"), max_length=255, unique=True) 
	text  = models.CharField(verbose_name=('Текст'), max_length=255)
	is_active = models.BooleanField(verbose_name=("Активність"), default=True)

	def __str__(self):
		return f"{self.text}"

	@classmethod
	def modeltranslation_fields(cls):
		fields = [
			'text',
		]
		return fields


	class Meta:
		verbose_name = ('Маркер')
		verbose_name_plural = ('Маркери')


class ItemManufacturer(models.Model):
	name  = models.CharField(verbose_name=('Назва'), max_length=255)
	is_active = models.BooleanField(verbose_name=("Активність"), default=True)

	@classmethod
	def modeltranslation_fields(cls):
		fields = [
		    'name',
		]
		return fields


	def __str__(self):
		return f"{self.name}"
	
	class Meta:
		verbose_name = ('Виробник')
		verbose_name_plural = ('Виробники')


class ItemBrand(models.Model):
	name = models.CharField(verbose_name=("Назва"), max_length=255)
	is_active = models.BooleanField(verbose_name=("Активність"), default=True)

	@classmethod
	def modeltranslation_fields(cls):
		fields = [
		    'name',
		]
		return fields

	def __str__(self):
		return f"{self.name}, {self.is_active}" 
	
	class Meta:
		verbose_name = ('Бренд')
		verbose_name_plural = ("Бренди")

from adminsortable.models import SortableMixin

class Item(
	SortableMixin,
	# models.Model,
	):
	objects      = ItemManager()
	# default_objects = models.Manager()
	
	meta_title   = models.TextField(verbose_name=("Мета заголовок"),          blank=True, null=True)
	meta_descr   = models.TextField(verbose_name=("Мета опис"),               blank=True, null=True)
	meta_key     = models.TextField(verbose_name=("Мета ключові слова"),      blank=True, null=True)

	title        = models.CharField(verbose_name=("Назва"), max_length=255, null=False)
	description  = models.TextField(verbose_name=("Опис"),                    blank=True, null=True)
	code         = models.CharField(verbose_name=("Артикул"), max_length=255,  blank=True, null=True, unique=True)   
	slug         = models.SlugField(verbose_name=("Ссилка"),  max_length=255, unique=True, blank=False, null=True)
	thumbnail    = models.ImageField(verbose_name=("Маленька картинка"), blank=True, upload_to="shop/items/thumbnails")
	markers      = models.ManyToManyField(verbose_name=("Маркери"), to='item.ItemMarker', related_name='items', blank=True)
	manufacturer = models.ForeignKey(verbose_name=("Виробник"), to="item.ItemManufacturer", blank=True, null=True, on_delete=models.SET_NULL, related_name='items')
	brand        = models.ForeignKey(verbose_name=("Бренд"), to='item.ItemBrand', related_name='items', on_delete=models.SET_NULL, null=True, blank=True)
	# old_price    = models.DecimalField(verbose_name=("Стара ціна"), max_digits=10, decimal_places=2, default=0)
	# price        = models.DecimalField(verbose_name=("Нова ціна"),  max_digits=10, decimal_places=2, default=0)
	# TODO: rest_framework.serializers.ModelSerializer чогось не серіалізує DecimalField

	old_price    = models.FloatField(verbose_name=("Стара ціна"), blank=True, null=True)
	new_price    = models.FloatField(verbose_name=("Актуальна ціна"), blank=True, null=True)
	currency     = models.ForeignKey(verbose_name=("Валюта"),    to="item.ItemCurrency",     related_name="items", on_delete=models.SET_NULL, help_text=("Якщо залишити порожнім, то буде встановлена валюта категорії, у якій знаходиться товар"), blank=True, null=True)

	if settings.MULTIPLE_CATEGORY:
		categories   = models.ManyToManyField(verbose_name=("Категорія"), to='item.ItemCategory', related_name="items", blank=True)    
	else:
		# category     = models.ForeignKey(verbose_name=("Категорія"), to='item.ItemCategory', related_name="items", on_delete=models.SET_NULL, blank=True, null=True)    
		category     = TreeForeignKey(verbose_name=("Категорія"), to='item.ItemCategory', related_name="items", on_delete=models.SET_NULL, blank=True, null=True)    

	in_stock     = models.ForeignKey(verbose_name=("Наявність"), to="item.ItemStock", on_delete=models.SET_NULL, blank=True, null=True, help_text='"Кількість" в пріорітеті над "наявністю"')
	amount       = models.PositiveIntegerField(verbose_name=("Кількість"), blank=True, null=True, default=None, help_text='"Кількість" в пріорітеті над "наявністю"')
	unit         = models.CharField(verbose_name=("Одиниці вимірювання"), blank=True, null=True, max_length=255)
	is_active    = models.BooleanField(verbose_name=("Активний"),      default=True,  help_text="Присутність товару на сайті в списку товарів")

	created      = models.DateTimeField(verbose_name=("Створений"), default=timezone.now)
	updated      = models.DateTimeField(verbose_name=("Оновлений"), auto_now_add=False, auto_now=True,  blank=True, null=True)

	order        = models.PositiveIntegerField(verbose_name=("Порядок"), default=0, editable=False, db_index=True)
	similars     = models.ManyToManyField(verbose_name=("Схожі товари"), to="self", blank=True)


	@classmethod
	def modeltranslation_fields(cls):
		fields = [
			'meta_title',
			'meta_descr',
			'meta_key',
			'title',
			'description',
		]
		return fields 


	class Meta: 
		verbose_name = ('Товар'); 
		verbose_name_plural = ('Товари')
		ordering = ['order']


	def __str__(self):
		return f"{self.title}, {self.slug}"

	def save(self, *args, **kwargs):
		# self.handle_currency(*args, **kwargs)
		self.handle_slug(*args, **kwargs)
		self.handle_availability(*args, **kwargs)
		super().save(*args, **kwargs)
		self.resize_thumbnail(self.thumbnail)

	def handle_slug(self, *args, **kwargs):
		if not self.slug:
			from transliterate.exceptions import LanguagePackNotFound, LanguageDetectionError
			try:
				slug = slugify(translit(self.title, reversed=True)) 
			except Exception as e:
				slug = f"{slugify(self.title)}"

			origin_slug = slug
			numb = 1
			while Item.objects.filter(slug=slug).exists():
				slug = f'{origin_slug}-{numb}'
				numb += 1
			self.slug = slug

	def handle_availability(self, *args, **kwargs):
		'''
		self.in_stock              == None  - безкінечний
		self.in_stock.availability == False - відсутній
		self.in_stock.availability == True  - присутній 

		self.amount == None                 - безкінечний
		self.amount == 0                    - відсутній
		self.amount > 0                     - присутній 

		'''

		available_stocks   = ItemStock.objects.filter(availability=True)
		unavailable_stocks = ItemStock.objects.filter(availability=False)

		if self.amount == 0:
			if unavailable_stocks.exists():
				self.in_stock = unavailable_stocks.first()
		# if self.amount == None or self.amount > 0:
		# 	if available_stocks.exists():
		# 		self.in_stock = available_stocks.first()
		# 	else:
		# 		self.in_stock == None 
		 
	def handle_currency(self, *args, **kwargs):
		if not self.currency:
			if settings.MULTIPLE_CATEGORY:
				if self.categories.all().exists():
					self.currency = self.categories.all().first().currency
				else:
					try:
						self.currency = ItemCurrency.objects.get(is_main=True)
					except:
						self.currency = ItemCurrency.objects.all().first()
			else:
				if self.category:
					self.currency = self.category.currency
				else:
					try:
						self.currency = ItemCurrency.objects.get(is_main=True)
					except:
						self.currency = ItemCurrency.objects.all().first()

	def resize_thumbnail(self, thumbnail):
		if thumbnail:
			width  = 400
			img    = Image.open(thumbnail.path)
			# height = 400
			height = int((float(img.size[1])*float((width/float(img.size[0])))))
			img    = img.resize((width,height), Image.ANTIALIAS)
			img.save(thumbnail.path) 

	def create_thumbnail_from_images(self):
		thumbnail = self.images.all().first().image
		# self.thumbnail = thumbnail
		# self.save()
		if thumbnail:
			# print(thumbnail)
			self.thumbnail.save(
				thumbnail.name.split("/")[-1], 
				ContentFile(thumbnail.read()),
			)

	def get_absolute_url(self):
		return reverse("item", kwargs={"slug": self.slug})

	@property
	def is_in_stock(self):
		if self.amount == 0:
			is_in_stock = False
		else:
			is_in_stock = True 
		return is_in_stock

	@property
	def price(self):
		if self.new_price:
			price = self.new_price
		elif self.old_price:
			price = self.old_price
		else:
			return 0
		
		# return price 
		# !!!!!!!!!!!!
		main_currency = ItemCurrency.objects.get(is_main=True)
		current_currency = self.currency
		# current_currency = self.category.currency
		# print('--------')
		if current_currency != main_currency:


			ratio = ItemCurrencyRatio.objects.filter(
				main=main_currency,
				compared=current_currency,
			)
			if ratio.exists():
				# print('main_currency: ', main_currency)
				ratio = ratio.first().ratio
				# print('\n')
				price = price / ratio


			ratio = ItemCurrencyRatio.objects.filter(
				main=current_currency,
				compared=main_currency,
			)
			if ratio.exists():
				# print('current_currency: ', current_currency)
				ratio = ratio.first().ratio
				price = price * ratio
		# print('price: ', price)
		# print('self.currency: ', self.currency)
		# print('self.price.new_price: ', self.new_price)
		# print('self.price.old_price: ', self.old_price)
		# print('__________')
		print(price)
		return price 

	@property
	def thumbnail_url(self):
		if self.thumbnail:
			url = self.thumbnail.url
		else:
			url = item_settings.NO_ITEM_IMAGE
		return url 

	@property
	def main_image(self):
		image = self.thumbnail
		# print(image)
		image = self.images.all().first()
		# print(image)
		return image

	def get_stars_total(self):
		stars_total = 0
		for review in self.reviews.all():
			stars_total += int(review.rating)
		return stars_total

	@property
	def rounded_stars(self):
		total = self.get_stars_total()
		try:
			stars = round(total/self.reviews.all().count())
		except:
			stars = 0
		return str(stars)

	@property
	def stars(self):
		total = self.get_stars_total()
		try:
			stars = total/self.reviews.all().count()
		except:
			stars = 0
		return str(stars)
	
	def set_category(self, categories):
		if settings.MULTIPLE_CATEGORY:
			for category in categories:
				self.categories.add(category)
		else:
			self.category = categories[-1]
		self.save()

	def get_categories(self, ):

		return categories 
	
	def in_cart(self, request):
		from box.shop.cart.models import CartItem
		from box.shop.cart.utils import get_cart
		in_cart = self.id in CartItem.objects.filter(cart=get_cart(request)).values_list('item__id', flat=True)
		return in_cart 


from django.db.models.signals import post_save, pre_save


class ItemCategory(MPTTModel):
	meta_title = models.TextField(verbose_name=("Мета заголовок"),     blank=True, null=True)
	meta_descr = models.TextField(verbose_name=("Мета опис"),          blank=True, null=True)
	meta_key   = models.TextField(verbose_name=("Мета ключові слова"), blank=True, null=True)
	slug       = models.SlugField(verbose_name=("Посилання"),          unique=True, max_length=255, null=True, blank=False)
	code       = models.CharField(verbose_name=("Код"), blank=True, null=True, max_length=255, help_text=("Код для прогера"))
	title      = models.CharField(verbose_name=("Назва"),  max_length=255, blank=False, null=False)
	thumbnail  = models.ImageField(verbose_name=("Картинка"), blank=True, null=True, upload_to='shop/category')
	alt        = models.CharField(verbose_name=("Альт до картинки"),   blank=True, null=True, max_length=255)
	description= models.TextField(verbose_name=("Опис"), blank=True, null=True)

	parent     = TreeForeignKey(verbose_name=("Батьківська категорія"), to='self', blank=True, null=True, on_delete=models.SET_NULL, related_name='subcategories')
	# parent     = models.ForeignKey(verbose_name=("Батьківська категорія"), to='self', blank=True, null=True, on_delete=models.SET_NULL, related_name='subcategories')

	currency   = models.ForeignKey(verbose_name=("Валюта"), to="item.ItemCurrency", blank=True, null=True, related_name="categories",  on_delete=models.SET_NULL)

	is_active  = models.BooleanField(verbose_name=("Чи активна"), default=True, help_text=("Присутність категорії на сайті"))

	created    = models.DateTimeField(verbose_name=("Створено"), default=timezone.now)
	updated    = models.DateTimeField(verbose_name=("Оновлено"), auto_now_add=False, auto_now=True, blank=True, null=True)

	# objects    = ItemCategoryManager()
	# TODO: визначити якого хуя з включеним ItemCategoryManager дочірні категорії  виводяться не ті шо треба, а всі підряд

	class Meta: 
		verbose_name = ('категорія'); 
		verbose_name_plural = ('категорії'); 
		unique_together = ('title', 'parent')
		
	def get_absolute_url(self):
		return reverse("item_category", kwargs={"slug": self.slug})

	@classmethod
	def modeltranslation_fields(cls):
		fields = [
			'meta_title',
			'meta_descr',
			'meta_key',
			'title',
			'alt',
			'description',
		]
		return fields 

	@property
	def thumbnail_path(self):
		thumbnail = ''
		if self.thumbnail:
			thumbnail = self.thumbnail.path
		return thumbnail

	@property
	def thumbnail_url(self):
		thumbnail = ''
		if self.thumbnail:
			thumbnail = self.thumbnail.url
		return thumbnail
	
	@property
	def parent_slug(self):
		slug = ''
		if self.parent:
			slug = self.parent.slug	
		return slug
	
	@property
	def parents(self):
		parent = self.parent 
		parents = [self, parent]
		# parents = [parent]
		if parent:
			while parent.parent:
				parent = parent.parent 
				parents.append(parent)
				# parents.insert(0, parent)
		# parents = reversed(parents)
		return parents[-1::-1]


	@property
	def tree_title(self):
		result = self.title
		# try:
		# 	full_path = [self.title]      
		# 	parent = self.parent
		# 	while parent is not None:
		# 		print(parent)
		# 		full_path.append(parent.title)
		# 		parent = parent.parent
		# 	result = ' -> '.join(full_path[::-1]) 
		# except Exception as e:
		# 	print(e)
		# 	result = self.title
		return result

	def __str__(self):     
		result = f'{self.title}'
		result = f'{self.tree_title} ({self.currency})'
		return result


	def save(self, *args, **kwargs):

		if self.currency:
			# try:
			# 	self.items.all().update(currency=self.currency)
			# except:
			# 	pass
			pass

		elif not self.currency:
			alls  = ItemCurrency.objects.all()
			mains = alls.filter(is_main=True)
			if mains.exists():
				self.currency = mains.first()
			elif alls.exists():
				self.currency = alls.first()


		title = self.title.lower().strip()
		# origin_title = title
		# numb = 1
		# while ItemCategory.objects.filter(title=title).exists():
		# 	title = f'{origin_title} ({numb})'
		# 	numb += 1
		self.title = title
		if not self.slug:
			try:
				slug = slugify(translit(self.title, reversed=True), allow_unicode=True) 
			except Exception as e:
				slug = slugify(translit(self.title, 'uk', reversed=True), allow_unicode=True) 
			except Exception as e:
				slug = slugify(translit(self.title, 'ru', reversed=True), allow_unicode=True) 
			except Exception as e:
				slug = slugify(self.title, allow_unicode=True)
			if slug == '':
				slug = slugify(self.title, allow_unicode=True)

			# numb = 1
			# origin_slug = slug 
			# while ItemCategory.objects.filter(slug=slug).exists():
			# 	slug = f'{origin_slug}-{numb}'
			# 	numb += 1



			self.slug  = slug
			cats = ItemCategory.objects.filter(slug=slug)
			# if cats.exists():
			# 	cat = cats.first()
			# print(slug)
			# print(cat)

		super().save(*args, **kwargs)


def generate_unique_slug(klass, field, item, *args, **kwargs):
	origin_slug = slugify(translit(field, reversed=True)) # slugify(field)
	unique_slug = origin_slug
	numb = 1
	obj = klass.objects.filter(slug=unique_slug)
	while obj.exists():
		obj = obj.first()
		unique_slug = f'{origin_slug}-{numb}'
		numb += 1
	return unique_slug


def item_image_folder(instance, filename):
	ext = filename.split('.')[-1]

	# foldername = instance.slug
	foldername = 'slug'

	# slug = instance.slug
	slug = 'slug'

	filename = slug + '.' + ext

	path = f"shop/items"
	path = '/'.join(['shop','items'])

	path = f"{foldername}/{filename}"
	path = '/'.join([foldername, filename])

	path = f"shop/items/{foldername}/{filename}"
	path = '/'.join(['shop', 'items', foldername, filename])

	return path 


class ItemImage(SortableMixin):

	item  = models.ForeignKey(verbose_name=("Товар"), to="item.Item", on_delete=models.SET_NULL, related_name='images', null=True)
	image = models.ImageField(verbose_name=('Ссилка зображення'), upload_to=item_image_folder, blank=True, null=True, default='shop/items/test_item.jpg')
	alt   = models.CharField(verbose_name=("Альт"), max_length=255, blank=True, null=True)
	order     = models.PositiveIntegerField(verbose_name=("Порядок"), default=0, editable=False, db_index=True)
	is_active = models.BooleanField(("Активність"), default=True)
	objects = ImageManager()

	def __str__(self):
		return "%s" % self.image
	
	@classmethod
	def modeltranslation_fields(cls):
		fields = [
		    'alt',
		]
		return fields


	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		# img = Image.open(self.image.path)
		# img = img.resize((400, 400), Image.ANTIALIAS)
		# img.save(self.image.path)

	class Meta: 
		verbose_name = ('Зображення товару'); 
		verbose_name_plural = ('Зображення товару'); 
		ordering = ['order',]


class ItemFeatureName(models.Model):
	name = models.CharField(verbose_name=("Назва характеристики"), max_length=255)
	slug = models.SlugField(verbose_name=("ЧПУ характеристики"), unique=True)

	def __str__(self):
		return f"{self.name}"
	@classmethod
	def modeltranslation_fields(cls):
		fields = [
		    'name',
		]
		return fields
	def save(self, *args, **kwargs):
		if not self.slug:
			try:
				slug = slugify(translit(self.title, reversed=True)) 
			except Exception as e:
				slug = f"{slugify(self.title)}"
			self.slug = slug
		super().save(*args, **kwargs)
	
	class Meta:
		verbose_name = 'назва характеристики'
		verbose_name_plural = 'назви характеристики'


class ItemFeature(models.Model):
	item     = models.ForeignKey(verbose_name="Товар", to="item.Item", related_name="features", on_delete=models.SET_NULL, blank=True, null=True)
	name     = models.ForeignKey(verbose_name="Назва характеристики", to="item.ItemFeatureName",blank=True, null=True, related_name='features', on_delete=models.SET_NULL)
	code     = models.CharField(verbose_name=("Код"), blank=True, null=True, max_length=255, help_text="Код для прямого звернення до характеристики в шаблоні")
	value    = models.TextField(verbose_name="Значення характеристики", blank=True, null=False)
	category = models.ForeignKey(verbose_name="Категорія характеристики", to="item.ItemFeatureCategory", related_name="items", on_delete=models.SET_NULL, blank=True, null=True)
	@classmethod
	def modeltranslation_fields(cls):
		fields = [
		    'value',
		]
		return fields
	def __str__(self):
		return f'{self.name}'

	class Meta:
		verbose_name = ('Характеристика товару')
		verbose_name_plural = ('Характеристики товару')


class ItemFeatureCategory(models.Model):
	parent = models.ForeignKey(verbose_name=("Батьківська категорія"), to='self', related_name='subcategories', blank=True, null=True, on_delete=models.SET_NULL)
	name   = models.CharField(verbose_name=("Назва категорії"), max_length=255, unique=True, blank=True, null=True)
	@classmethod
	def modeltranslation_fields(cls):
		fields = [
		    'name',
			
		]
		return fields

	def __str__(self):
		return f"{self.name}"

	class Meta:
		verbose_name = 'Категорія характеристики'
		verbose_name_plural = 'Категорії характеристики'


class ItemReview(models.Model):
	item    = models.ForeignKey(verbose_name=("Товар"),  blank=True, null=True, to='item.Item', on_delete=models.SET_NULL, related_name="reviews",)
	user    = models.ForeignKey(verbose_name=("Автор"),  blank=True, null=True, to=User, on_delete=models.SET_NULL, related_name="reviews",)
	text    = models.CharField(verbose_name=("Відгук"),  blank=True, null=True, max_length=255)
	phone   = models.CharField(verbose_name=("Телефон"), blank=True, null=True, max_length=255)
	email   = models.CharField(verbose_name=("E-mail"),  blank=True, null=True, max_length=255)
	name    = models.CharField(verbose_name=("Ім'я"),    blank=True, null=True, max_length=255)
	rating  = models.CharField(verbose_name=("Оцінка"),  blank=True, null=True, max_length=255)
	created = models.DateTimeField(verbose_name=("Дата створеня"), auto_now=False, default = timezone.now)
	updated = models.DateTimeField(verbose_name=("Дата останнього редагування"), auto_now=True, auto_now_add=False)

	def __str__(self):
		return f"{self.text}{self.rating}"

	class Meta:
		verbose_name = ('Відгук')
		verbose_name_plural = ('Відгуки')






