from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from cart.models import *

# Create your views here.

def home(reqset):
    product = Product.objects.filter(is_new=True).order_by('-created_at')[:5]
    product_sale = Product.objects.filter(is_sale=True).order_by('-created_at')[:5] if Product.objects.filter(is_sale=True).exists() else None

    return render(reqset, 'shop/index.html', {'product': product, 'product_sale': product_sale})

def single_product(reqset,pk):
    single_product = Product.objects.get(id=pk)
    return render(reqset,'sohp/single-product.html',{'single':single_product})

def products_page(reqset):
    products = Product.objects.all()
    context = {
        'product':products
    }
    return render(reqset,'shop/Products.html',context)
def products_page_sale(reqset):
    product = Product.objects.all()
    context = {
        'product':product
    }
    return render(reqset,'shop/Products_sale.html',context)
def search_results(request):
    query = request.GET.get('query')
    results = []

    if query:
        results = Product.objects.filter(name__icontains=query)  # جستجو بر اساس نام محصول

    return render(request, 'search_results.html', {'results': results, 'query': query})
def ajax_add_to_cart(request):
    if request.method == 'POST' and request.user.is_authenticated:
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)

        cart, created = Cart.objects.get_or_create(user=request.user)
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += 1
            item.save()

        return JsonResponse({'success': True, 'message': 'محصول اضافه شد به سبد خرید'})
    else:
        return JsonResponse({'success': False, 'message': 'لطفاً وارد شوید'})

def get_total(self):
        total = 0
        for item_id, item_data in self.cart.items():
            product = Product.objects.get(id=int(item_id))
            total += float(product.price) * item_data['qty']
        return total
def update(self, product, quantity):
        productid = str(product)
        productqty = int(quantity)

        ourcart = self.cart
        ourcart[productid] = productqty

        self.session.modified = True

        alake = self.cart
        return alake
def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = (request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id,quantity=product_qty)

        response = JsonResponse({'qty': product_qty})
        return response
def cart_detail(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        total = 0
        total = cart.get_total()
        quantities = cart.get_quants()
    else:
        cart = None
    
    context = {'cart': cart,
               'total': total,
               'quantities': quantities
               }
    return render(request, 'cart/cart_summary.html',context)

@require_POST
def ajax_remove_from_cart(request):
    if request.user.is_authenticated:
        item_id = request.POST.get('item_id')
        try:
            item = CartItem.objects.get(id=item_id, cart__user=request.user)
            item.delete()
            return JsonResponse({'success': True, 'message': 'محصول از سبد حذف شد'})
        except CartItem.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'آیتم پیدا نشد'})
    return JsonResponse({'success': False, 'message': 'لطفاً وارد شوید'})
