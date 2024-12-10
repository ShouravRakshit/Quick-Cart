from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from products.models import Product
from .models import Cart, CartItem
from django.views.decorators.http import require_POST

# Create your views here.

@require_POST
def cart_add(request, product_id):
    cart_id = request.session.get('cart_id')

    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create()
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    product = get_object_or_404(Product, id=product_id)
    try:
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
        cart_item.save()
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)}, status=500)

    response_data = {  
        "status": 'success',
        "message": f"Added {product.name} to cart",
    }

    return JsonResponse(response_data)
    
def cart_detail(request):
    cart_id = request.session.get('cart_id')
    cart = None

    if cart_id:
        cart = Cart.objects.get(id=cart_id)

    return render(request, 'cart/cart_detail.html', {'cart': cart})
