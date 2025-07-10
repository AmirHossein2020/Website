from django.shortcuts import render
from cart.models import *
from django.http import JsonResponse
from django.views.decorators.http import require_POST
# Create your views here.

def ajax_add_to_cart(request):
    if request.method == 'POST' and request.user.is_authenticated:
        product_id = request.POST.get('product_id')
        product = Products.objects.get(id=product_id)

        cart, created = Cart.objects.get_or_create(user=request.user)
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += 1
            item.save()

        return JsonResponse({'success': True, 'message': 'محصول اضافه شد به سبد خرید'})
    else:
        return JsonResponse({'success': False, 'message': 'لطفاً وارد شوید'})


def cart_detail(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        cart = None

    context = {'cart': cart}
    return render(request, 'Cart/Cart.html',context)

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
