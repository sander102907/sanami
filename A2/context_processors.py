from products.cart import Cart

def cartAmount(request):
    cart = Cart(request)
    return {
        'cart': cart
}
