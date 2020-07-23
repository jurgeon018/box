from django.urls import path, include 
from .views import * 


urlpatterns = [
  path('items/', ItemList.as_view()),
  path('items/<pk>/', ItemDetail.as_view()),
  path('item_attributes/', ItemAttributeList.as_view()),
  path('item_attributes/<pk>/', ItemAttributeRetrieve.as_view()),
  
  path('create_review/', create_review),
  path('get_items/', get_items, name='get_items'),
  path('get_item/', get_item, name='get_item'),
]





