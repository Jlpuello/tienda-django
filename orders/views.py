from django.shortcuts import render

from carts.utils import get_or_create_cart

from .models import Order


def order(request):
    cart = get_or_create_cart(request)
    order = Order.objects.filter(cart=cart).first()

    if order is None and request.user.is_authenticated:
        order = Order.objects.create(cart=cart, user=request.user)

    if order:
        request.session['order_id'] = order.order_id

    return render (request, 'orders/order.html', {
        'cart':cart,
        'order':order,
    })