from django.contrib import admin
from .models import Item, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')

@admin.register(Order)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_amount')

