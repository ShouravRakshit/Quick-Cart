from django.shortcuts import get_object_or_404, render, redirect

from cart.models import Cart
from orders.forms import OrderCreateForm
from orders.models import OrderItem

# Create your views here.

def order_create(request):
    cart = None
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart = get_object_or_404(Cart, id=cart_id)

        if not cart or not cart.items.all():
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
                    quantity=item.quantity)
            cart.delete()
            del request.session['cart_id']
            return redirect('orders:order_confirmation', order.id)
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/order_create.html', {'cart': cart, 'form': form})