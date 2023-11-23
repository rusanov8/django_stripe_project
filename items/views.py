from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.conf import settings


from items.models import Item
from items.services import create_stripe_session


class ItemListView(ListView):
    model = Item


class ItemDetailView(DetailView):
    model = Item


def buy_product(request, pk):
    item = get_object_or_404(Item, pk=pk)
    session = create_stripe_session(item)
    print(session.url)
    return JsonResponse({'session_id': session.id})







