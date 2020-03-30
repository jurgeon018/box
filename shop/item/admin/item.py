from .imports import * 
from django.utils.translation import gettext_lazy as _






class ItemAdmin(
    BaseAdmin,
    TabbedTranslationAdmin, 
    ): 
    # changelist  
    # change_list_template = 'item_change_list.html'
    def change_category(self, request, queryset):
        initial = {
            'model':ItemCategory,
            'attr':'category',
            'action_value':'change_category',
            'action_type':'add',
            'text':_('Нова категорія буде застосована для наступних позиций:'),
            'title':_("Зміна категорії"),
            'message':_('Категорія {0} була застосована до {1} товарів'),
        }
        return move_to(self, request, queryset, initial)

    def change_brand(self, request, queryset):
        initial = {
            'model':ItemBrand,
            'attr':'brand',
            'action_value':'change_brand',
            'action_type':'add',

            'text':_('Новий бренд буде застосований для наступних позиций:'),
            'title':_("Зміна бренду"),
            'message':_('Бренд {0} був застосований до {1} товарів'),
        }
        return move_to(self, request, queryset, initial)

    def add_markers(self, request, queryset):
        initial = {
            'model':ItemMarker,
            'attr':'markers',
            'action_value':'add_markers',
            'action_type':'add',
            'text':_('Нові маркери будуть застосовані для наступних позиций:'),
            'title':_("Додавання маркерів"),
            'message':_('Маркери {0} були застосовані до {1} товарів'),
        }
        return move_to(self, request, queryset, initial)
    
    def remove_markers(self, request, queryset):
        initial = {
            'model':ItemMarker,
            'attr':'markers',
            'action_value':'remove_markers',
            'action_type':'remove',
            'text':_('Нові маркери будуть забрані з наступних позиций:'),
            'title':_("Видалення маркерів з товарів"),
            'message':_('Маркери {0} були забрані з {1} товарів'),
        }
        return move_to(self, request, queryset, initial)

    change_category.short_description = _("Змінити категорію")
    add_markers.short_description     = _("Додати маркери")
    remove_markers.short_description  = _("Забрати маркери")
    change_brand.short_description    = _("Змінити бренд")
    actions = [
        "is_active_on",
        "is_active_off",
        # 'export_items',
        'admin_export_items_to_xlsx',
        "admin_export_items_photoes",
        "admin_delete_items_photoes",
        "admin_delete_items_features",
        "change_category",
        "change_brand",
        "add_markers",
        "remove_markers",
        'export_admin_action',
    ]
    search_fields = [
        'title',
        'code',
    ]
    list_filter = [
        # "category",
        # ('category', ItemCategoryTreeRelatedFieldListFilter),
        CategoryFilter,
        MarkersFilter,
        BrandFilter,
    ]
    list_display = [
        # 'id',
        "order",
        'show_image',
        'title',
        'new_price',
        'currency',
        'amount',
        # 'units',
        # 'in_stock',
        'is_active',
        # "clone_link",
        'show_site_link',
        "show_edit_link",
        "show_delete_link",
    ]
    list_editable = [
        'new_price',
        'currency',
        'amount',
        # 'units',
        # TODO: змінити ширину інпута
        'is_active',
    ]
    list_display_links = [
        'order',
        'title',
    ]
    # changeform
    # change_form_template = 'item_change_form.html'
    # form = ItemForm
    resource_class = ItemResource
    autocomplete_fields = [
        # 'similars',
        'markers',
        'brand',
        'in_stock',
        'currency',
    ]
    if settings.MULTIPLE_CATEGORY:
        autocomplete_fields.append('categories')
    else:
        autocomplete_fields.append('category')
    prepopulated_fields = {
        "slug": ("title",),
        # "code": ("title",),
    }
    inlines = [
        ItemImageInline,
        ItemFeatureStackedInline,
        ItemOptionInline,
        ItemReviewInline, 
    ]  
    item_fields = [
        'title',
        "brand",
        'in_stock',
        'currency',
        "markers",   # TODO: Додаються всі маркери
        # "similars",   # TODO: : Додаються всі товари
        (
        'old_price',
        'new_price',
        ),
        (
        "units",
        'amount',
        ),
        'is_active',
        'description',
        'image',
        'code',
        'created',
        'updated',
    ]
    if settings.MULTIPLE_CATEGORY:
        item_fields.insert(2 ,'categories')
    else:
        item_fields.insert(2 ,'category')
    fieldsets = [
        [('ОСНОВНА ІНФОРМАЦІЯ'), {
            'fields':item_fields
        }],
        seo,
    ]    

