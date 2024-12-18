from .models import Cart

def cart_item_count(request):
    """
    Calculate the total cart item count and check if it exceeds 9.
    """
    cart_id = request.session.get('cart_id')
    total_items = 0

    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
            total_items = sum(item.quantity for item in cart.items.all())
        except Cart.DoesNotExist:
            pass  # No cart exists, total remains 0

    return {
        'cart_item_count': min(total_items, 9),  # Display up to 9
        'cart_count_exceeded': total_items > 9,  # Show '+' if exceeded
    }
