from django.urls import path 
from .views import * 

urlpatterns = [
    path('autocomplete/', autocomplete, name='autocomplete'),

]
