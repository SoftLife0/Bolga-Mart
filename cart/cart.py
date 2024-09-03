from store.models import Product

class Cart():
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price':str(product.price)}
        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        # Get ids from cart 
        product_ids = self.cart.keys()
        # Use ids to lookup products in database
        products = Product.objects.filter(id__in=product_ids)   
        # Return looked up product    
        return products 