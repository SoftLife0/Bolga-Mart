from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# view for cart 
def cart_summary(request):
    # Get the cart 
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    context = {'cart_products': cart_products, 'quantities': quantities}
    return render(request, "cart_summary.html", context)

def cart_add(request):
    cart = Cart(request)
    # test for post
    if request.POST.get('action') == 'post':
        # get product id
        product_id = int(request.POST.get('product_id'))
        # lookup product in db
        product = get_object_or_404(Product, id=product_id)
        # save to session
        cart.add(product=product)
        # Get cart quantity
        cart_quantity = cart.__len__()
        # return response
        response = JsonResponse({'qty': cart_quantity})
        return response
    return render(request, "cart_add.html", {})


def cart_delete(request):
    return render(request, "cart_delete.html", {})

def cart_update(request):
    return render(request, "cart_update.html", {})