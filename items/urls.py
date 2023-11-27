from django.urls import path
from .views import (ItemListView, ItemDetailView, make_product_payment,
                    success_payment, add_to_order, OrderDetailView, OrderDeleteView, make_order_payment)
from items.apps import ItemsConfig


app_name = ItemsConfig.name

urlpatterns = [
    path('', ItemListView.as_view(), name='item_list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('items/<int:pk>/buy/', make_product_payment, name='make_product_payment'),
    path('success_payment/', success_payment, name='success_payment'),
    path('items/<int:pk>/add_to_order/', add_to_order, name='add_to_order'),
    path('orders/<int:order_pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('orders/<int:order_pk>/buy/', make_order_payment, name='make_order_payment'),
    path('orders/<int:order_pk>/delete/', OrderDeleteView.as_view(), name='delete_order'),
]