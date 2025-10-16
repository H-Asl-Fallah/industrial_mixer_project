from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

@login_required
def order_create(request):
    cart = Cart(request)
    if not cart:
        return redirect('shop:product_list')

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # Clear the cart
            cart.clear()
            # Redirect to profile page to see the new order
            return redirect('profiles:profile') 
    else:
        form = OrderCreateForm()
    return render(request,
                  '../templates/create.html',
                  {'cart': cart, 'form': form})
