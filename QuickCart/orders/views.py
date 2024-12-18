from django.shortcuts import get_object_or_404, render, redirect

from cart.models import Cart
from orders.forms import OrderCreateForm
from orders.models import OrderItem, Order

# Create your views here.

def order_create(request):
    cart_id = request.session.get('cart_id')
    cart = None
    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            pass

    # Redirect if cart is None or has no items
    if not cart or not cart.items.exists():
        return redirect('cart:cart_detail')

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity,
                )
            # Delete cart after order is created
            cart.delete()
            request.session.pop('cart_id', None)  # Remove cart_id from session
            return redirect('orders:order_confirmation', order.id)
    else:
        form = OrderCreateForm()

    return render(request, 'order/order_create.html', {'cart': cart, 'form': form})


def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order/order_confirmation.html', {'order': order})
