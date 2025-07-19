from django.shortcuts import render, get_object_or_404
from .cart import Cart # مطمئن شوید که کلاس Cart را از فایل cart.py ایمپورت کرده‌اید
from website.models import Product # ایمپورت مدل Product
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.

def cart_summary(request):
    cart = Cart(request)
    cart_products = []
    quantities = {}
    total = 0

    # `cart.get_prods()` و `cart.get_quants()` و `cart.get_total()` 
    # باید از کلاس `cart.py` شما آمده باشند
    # اگر منطق سبد خرید شما به گونه‌ای دیگر است، آن را اینجا تطبیق دهید
    
    # فرض می‌کنیم ساختار داخلی Cart شما به این شکل است که
    # آیتم‌ها را در سشن نگهداری می‌کند و شامل product_id و quantity است.
    # برای نمایش، باید جزئیات محصول را از دیتابیس بگیریم.
    
    product_ids_in_cart = cart.cart.keys() # فرض می‌کنیم کلیدها product_id هستند
    products_in_cart = Product.objects.filter(id__in=product_ids_in_cart)

    for p in products_in_cart:
        qty = cart.cart[str(p.id)]['qty'] # فرض می‌کنیم qty اینجوری ذخیره شده
        cart_products.append(p)
        quantities[p.id] = qty
    
    total = cart.get_total() # این تابع باید در کلاس Cart شما تعریف شده باشد

    context = {
        'cart_products': cart_products,
        'quantities': quantities,
        'total': total,
    }
    return render(request, "cart/cart_summary.html", context)


# این توابع require_POST هستند و برای AJAX استفاده می‌شوند
@require_POST
def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        
        cart.add(product=product, quantity=product_qty)

        cart_quantity = cart.__len__() # تعداد کل آیتم‌های منحصر به فرد در سبد

        # بازگرداندن پاسخ JSON
        return JsonResponse({'qty': cart_quantity, 'success': True, 'message': 'محصول به سبد اضافه شد.'})
    return JsonResponse({'success': False, 'message': 'درخواست نامعتبر.'}, status=400)

@require_POST
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id') # اینجا product_id در واقع item_id است که از data-item-id می‌آید
        cart.delete(product=product_id) # این تابع باید در کلاس Cart شما وجود داشته باشد

        cart_quantity = cart.__len__()
        return JsonResponse({'qty': cart_quantity, 'success': True, 'message': 'محصول از سبد حذف شد.'})
    return JsonResponse({'success': False, 'message': 'درخواست نامعتبر.'}, status=400)


@require_POST
def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id') # اینجا product_id در واقع item_id است
        product_qty = int(request.POST.get('product_qty'))
        
        cart.update(product=product_id, quantity=product_qty) # این تابع باید در کلاس Cart شما وجود داشته باشد

        cart_quantity = cart.__len__()
        return JsonResponse({'qty': cart_quantity, 'success': True, 'message': 'تعداد محصول به‌روز شد.'})
    return JsonResponse({'success': False, 'message': 'درخواست نامعتبر.'}, status=400)