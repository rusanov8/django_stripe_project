from django.db import models


# Create your models here.
class Item(models.Model):

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



