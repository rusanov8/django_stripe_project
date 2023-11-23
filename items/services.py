import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_stripe_session(item):
    """
       Create a Stripe payment session for the specified course.
       """

    product = stripe.Product.create(
        name=item.name
    )

    price = stripe.Price.create(
        unit_amount=int(item.price * 100),
        currency="usd",
        product=product.id
    )

    session = stripe.checkout.Session.create(
        success_url=f"http://127.0.0.1:8000/items/{item.id}",
        line_items=[
            {
                "price": price.id,
                "quantity": 2,
            },
        ],
        mode="payment",
    )

    return session




