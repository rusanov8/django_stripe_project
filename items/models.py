from django.db import models


class Item(models.Model):
    """
       Модель для представления товара.
    """

    CURRENCY_CHOICES = (
        ('RUB', 'RUB'),
        ('USD', 'USD')
    )

    name = models.CharField(max_length=255, verbose_name='Наименование', db_index=True)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, verbose_name='Валюта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        db_table = 'items'


class Order(models.Model):
    """
        Модель для представления заказа.
    """

    items = models.ManyToManyField(Item, verbose_name='Товары')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Общая стоимость')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        db_table = 'orders'


class OrderItem(models.Model):
    """
        Модель для представления позиции товара в заказе.
    """

    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE, verbose_name='Заказ')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество товаров')

    def get_total_price(self):
        return self.item.price * self.quantity

    class Meta:
        db_table = 'order_item'
