from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Order, OrderItem, User_distributor
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json
from .models import *
# Create your views here.

def index(request):
    ctgs=categorie.objects.all()
    galls=gallery.objects.all()
    print(ctgs)
    context={'ctgs':ctgs,'galls':galls}
    return render(request, 'index.html',context)

def categories(request):
    ctgs=categorie.objects.all()
    context={'ctgs':ctgs}
    return render(request, 'categories.html',context)

def products(request, slug=None):
    # blogs=Blogs.objects.all()
    pros=Product.objects.filter(categorie_prod=slug)
    context={'pros':pros}
    return render(request, 'products.html',context)

def blogs(request):
    blogs=Blogs.objects.all()
    context={'blogs':blogs}
    return render(request, 'blog.html',context)

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
