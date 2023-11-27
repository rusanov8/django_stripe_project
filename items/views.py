from django.http import JsonResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView


from items.models import Item, Order, OrderItem
from items.services import create_product_stripe_session, create_order_stripe_session
from items.converter import convert_value


class ItemListView(ListView):
    """
        Представление для отображения списка товаров.
    """

    model = Item


class ItemDetailView(DetailView):
    """
        Представление для отображения деталей товара.
    """

    model = Item


def make_product_payment(request, pk):
    """
       Обрабатывает запрос на оплату товара и перенаправляет пользователя на страницу оплаты Stripe.
    """

    item = get_object_or_404(Item, pk=pk)
    session_url = create_product_stripe_session(item)
    return redirect(session_url)


def success_payment(request):
    """
        Отображает страницу успешной оплаты.
    """
    return render(request, 'items/success_payment.html')


def add_to_order(request, pk):
    """
       Обрабатывает запрос на добавление товара в заказ.
    """

    item = get_object_or_404(Item, pk=pk)

    # Получаем или создаем заказ в текущей сессии
    order_pk = request.session.get('order_pk')
    order, created = Order.objects.get_or_create(pk=order_pk)

    # Получаем или создаем объект OrderItem для данного товара
    order_item, item_created = OrderItem.objects.get_or_create(order=order, item=item)

    # Если товар уже существует в заказе, увеличиваем количество
    if not item_created:
        order_item.quantity += 1
        order_item.save()

    # Конвертируем стоимость товара в рубли
    order.total_amount += convert_value(item.price, item.currency)
    order.save()

    # Сохраняем id заказа в сессии
    if created:
        request.session['pk'] = order.id

    return redirect('items:item_detail', pk=pk)


class OrderDetailView(DetailView):
    """
        Представление для отображения деталей заказа.
    """

    model = Order

    def get_object(self, queryset=None):
        order_pk = self.kwargs.get('order_pk')
        order = Order.objects.filter(pk=order_pk).first()
        return order


def make_order_payment(request, order_pk):
    """
       Обрабатывает запрос на оплату заказа и перенаправляет пользователя на страницу оплаты Stripe.
    """

    order = get_object_or_404(Order, pk=order_pk)
    session_url = create_order_stripe_session(order)
    return HttpResponseRedirect(session_url)


class OrderDeleteView(DeleteView):
    """
      Представление для удаления заказа.
    """

    model = Order
    success_url = reverse_lazy('items:item_list')
    template_name = 'items/order_confirm_delete.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Order, pk=self.kwargs['order_pk'])






