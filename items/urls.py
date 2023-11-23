from django.urls import path
from .views import ItemListView, ItemDetailView, buy_product
from items.apps import ItemsConfig


app_name = ItemsConfig.name

urlpatterns = [
    path('', ItemListView.as_view(), name='item_list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('buy/<int:pk>/', buy_product, name='buy_item'),

]
