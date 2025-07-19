# cart/cart.py
from website.models import Product # فرض می‌کنیم مدل Product در website.models قرار دارد

class Cart():
    def __init__(self, request):
        self.session = request.session
       
        cart = self.session.get('session_key')

        
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

       
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['qty'] = int(self.cart[product_id]['qty']) + int(quantity)
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': int(quantity)}
        
        self.session.modified = True

    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())

    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products

    def get_quants(self):
        quantities = {}
        for item_id, item_data in self.cart.items():
            quantities[int(item_id)] = item_data['qty']
        return quantities

    def get_total(self):
        total = 0
        for item_id, item_data in self.cart.items():
            product = Product.objects.get(id=int(item_id))
            total += float(product.price) * item_data['qty']
        return total

    def delete(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

    def update(self, product_id, quantity):
        product_id = str(product_id)
        if product_id in self.cart:
            self.cart[product_id]['qty'] = quantity
            self.session.modified = True

