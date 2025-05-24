from django.shortcuts import render
from website.models import *
from website.forms import SearchForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
# Create your views here.

def home(request):

    labtops = Product.objects.filter(category = 1)
    Tshirts = Product.objects.filter(category = 2)
    jewellerys = Product.objects.filter(category = 3)
    context = {'labtops':labtops,
               'Tshirts':Tshirts,
               'jewellerys':jewellerys}
    return render(request, 'home.html', context)

def serh(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
         SearchText = searchForm.cleaned_data['SearchText']
         citys = Product.objects.filter(name__contains=SearchText)
    else:
        citys = Product.objects.all()
    context = {
        'searchForm':searchForm
    }

    return render(request, 'base.html', context)


def category(request,cat):
    cat = cat.replace("-", " ")
    try:
        category = Category.objects.get(name= cat)
        products = Product.objects.filter(category = category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        return render(request, 'category.html', {})

def category_summary(request):
    all_products = Category.objects.all()
    return render(request, 'category_summary.html',{'category': all_products})

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'singl.html', {'product': product})


from django.http import JsonResponse
from .models import Product, Cart, CartItem

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


def cart_detail(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        cart = None

    context = {'cart': cart}
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


def search_products(request):
    query = request.GET.get('q')
    results = Product.objects.filter(name__icontains=query) if query else []
    return render(request, 'search.html', {'results': results, 'query': query})


def electronic(request):
    return render(request, 'electronic.html')

def fashion(request):
    return render(request, 'fashion.html')

def jewellery(request):
    return render(request, 'jewellery.html')


