from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from orders.models import Order

@login_required
def profile_view(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, '../templates/profile.html', {'orders': orders})
