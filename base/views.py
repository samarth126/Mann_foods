from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Order, OrderItem, User_distributor
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json
# Create your views here.

def index(request):
    return render(request, 'index.html',{})

def blogs(request):
    return render(request, 'blog.html',{})

def blog_detail(request):
    return render(request, 'blog-details.html',{})


@login_required
def order(request):
    products = Product.objects.all()

    return render(request, 'order.html', {'products': products, })


def place_order(request):
    if request.method == 'POST':
        distributor_id = request.user.user_distributor
        print(distributor_id)
        # distributor = User_distributor.objects.get(user=distributor_id)
        order = Order.objects.create(distributor_name=distributor_id)
        data_received = json.loads(request.body)
        lis = data_received['data']
        for l in lis:

            pr_id = l['id']
            product = Product.objects.get(id=pr_id)
            quant = l['quantity']
            OrderItem.objects.create(
                order=order, product=product, quantity=quant)
        return HttpResponse("Order Placed Succesfully")
