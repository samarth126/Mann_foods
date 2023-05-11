from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Order, OrderItem, User_distributor
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
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

#view to signup distributer
def signup_distributor(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        company_name = request.POST['user_companyname']
        mobile = request.POST['user_mobile']
        address = request.POST['user_address']

        user = User.objects.create_user(username=username, password=password)
        distributor = User_distributor(
            user=user, user_companyname=company_name, user_mobile=mobile, user_address=address)
        distributor.save()

        # Redirect to the desired page after successful signup
        return HttpResponse("successfully created")

    return render(request, 'signup.html')


def login_distributor(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the distributor's dashboard or desired page after login
            return redirect('order')

    return render(request, 'login.html')



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
