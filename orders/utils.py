from .models import Order 

def get_or_create_order(cart, request):
    order = cart.order 

    if order is None and request.user.is_authenticated:
        order = Order.objets.create(cart=cart, user=request.user)ç
    
    if order:
        request.session['order_id'] = order.order_id

    return order 