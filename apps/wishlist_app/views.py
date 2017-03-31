from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib import messages
from .models import Wishlist, Product

# Create your views here.
def index(request):
    context = {
        "my_wishes": Wishlist.objects.filter(wisher_id=request.session['user_id']),
        "other_wishes": Product.objects.exclude(adder_id=request.session['user_id'])
    }
    return render(request, 'wishlist_app/dashboard.html', context)

def add_item_page(request):
    return render(request, 'wishlist_app/add_item_page.html')

def add_item(request):
    if request.method == "POST":
        html_item = request.POST['item']
        if len(html_item)<1:
            messages.error(request, 'Entry name cannot be empty!')
            return redirect('wishlist:add_item_page')
        if len(html_item)<3:
            messages.error(request, 'Entry must be at least 3 characters!')
            return redirect('wishlist:add_item_page')
        else:
            try:
                product = Product.objects.create(product=html_item, adder=request.session['user_id'])
                Wishlist.objects.create(wisher_id=request.session['user_id'], wishitem_id=product.id)
                return redirect('wishlist:home')
            except:
                messages.error(request, 'Item already exists!')
    else:
        messages.error(request, 'INVALID ENTRY')
        return redirect('wishlist:home')

def add_to_list(request, item_id, adder_id):
    Wishlist.objects.get(wishitem_id=item_id, wisher_id=request.session['user_id'])
    return redirect('wishlist:home')

def remove_item(request, item_id):
    Wishlist.objects.get(id=item_id).delete()
    return redirect('wishlist:home')

def wish_item(request, item_id):
    context = {
        "wishitem": Wishlist.objects.get(wishitem_id=item_id)
    }
    return render(request, 'wishlist_app/wish_item.html', context)
