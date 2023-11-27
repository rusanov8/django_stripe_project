import stripe
from django.conf import settings
from django.shortcuts import redirect

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_product_stripe_session(item):
    """
        Создает сеанс оплаты Stripe для указанного товара.
    """

    product = stripe.Product.create(
        name=item.name
    )

    if item.currency == 'RUB':
        currency = 'rub'
    else:
        currency = 'usd'

    price = stripe.Price.create(
        unit_amount=int(item.price * 100),
        currency=currency,
        product=product.id
    )

    session = stripe.checkout.Session.create(
        success_url=f"http://127.0.0.1:8000/success_payment/",
        line_items=[
            {
                "price": price.id,
                "quantity": 1,
            },
        ],
        mode="payment",
    )

    return session.url


def create_order_stripe_session(order):
    """
        Создает сеанс оплаты Stripe для заказа.
    """

    product = stripe.Product.create(
        name=f'Заказ {order.id}'
    )

    price = stripe.Price.create(
        unit_amount=int(order.total_amount * 100),
        currency='rub',
        product=product.id
    )

    session = stripe.checkout.Session.create(
        success_url=f"http://127.0.0.1:8000/success_payment/",
        line_items=[
            {
                "price": price.id,
                "quantity": 1,
            },
        ],
        mode="payment",
    )
    return session.url
