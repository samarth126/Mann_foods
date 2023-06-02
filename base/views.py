from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Order, OrderItem, User_distributor
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
import json
from .models import *
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test
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



def distributor_reg(request):
    if request.method == 'POST':
        # Desired area for agency
        applicant_state_name = request.POST['applicant_state_name']
        applicant_district_name = request.POST['applicant_district_name']
        applicant_tulka = request.POST['applicant_tulka']

        # Personal info
        personal_name = request.POST['personal_name']
        personal_age = request.POST['personal_age']
        personal_address = request.POST['personal_address']
        personal_pincode = request.POST['personal_pincode']
        personal_companyname = request.POST['personal_companyname']
        personal_mobile = request.POST['personal_mobile']
        personal_alt_mobile = request.POST['personal_alt_mobile']
        personal_telephone = request.POST['personal_telephone']
        personal_email = request.POST['personal_email']
        personal_educational_details = request.POST['personal_educational_details']

        # Partner info
        partner_name = request.POST['partner_name']
        partner_address = request.POST['partner_address']
        partner_pincode = request.POST['partner_pincode']
        partner_mobile = request.POST['partner_mobile']
        partner_alt_mobile = request.POST['partner_alt_mobile']
        partner_telephone = request.POST['partner_telephone']
        partner_email = request.POST['partner_email']

        # Other info
        applicant_experience = request.POST['applicant_experience']
        applicant_storage_info = request.POST['applicant_storage_info']
        applicant_transport_info = request.POST['applicant_transport_info']
        applicant_invesment_capacity = request.POST['applicant_invesment_capacity']

        storage_check = request.POST['storage_option']
        if(storage_check == "no"):
            applicant_storage_info="No_storage"
        else:
            applicant_storage_info=applicant_storage_info

        transport_check = request.POST['transport_option']
        if(transport_check == "no"):
            applicant_transport_info="No_transport"
        else:
            applicant_transport_info=applicant_transport_info 

        # Saving the distributor data to the model
        applicant = Distributor_Applicants(
            applicant_state_name=applicant_state_name,
            applicant_district_name=applicant_district_name,
            applicant_tulka=applicant_tulka,
            personal_name=personal_name,
            personal_age=personal_age,
            personal_address=personal_address,
            personal_pincode=personal_pincode,
            personal_companyname=personal_companyname,
            personal_mobile=personal_mobile,
            personal_alt_mobile=personal_alt_mobile,
            personal_telephone=personal_telephone,
            personal_email=personal_email,
            personal_educational_details=personal_educational_details,
            partner_name=partner_name,
            partner_address=partner_address,
            partner_pincode=partner_pincode,
            partner_mobile=partner_mobile,
            partner_alt_mobile=partner_alt_mobile,
            partner_telephone=partner_telephone,
            partner_email=partner_email,
            applicant_experience=applicant_experience,
            applicant_storage_info=applicant_storage_info,
            applicant_transport_info=applicant_transport_info,
            applicant_invesment_capacity=applicant_invesment_capacity
        )
        applicant.save()
        print(storage_check, transport_check)
    context={}
    return render(request,'reservation.html',context)




#view to signup distributer
def signup_distributor(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            password = request.POST['password']
            company_name = request.POST['user_companyname']
            mobile = request.POST['user_mobile']
            address = request.POST['user_address']

            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            distributor = User_distributor(
                user=user, user_companyname=company_name, user_mobile=mobile, user_address=address)
            distributor.save()

            # Redirect to the desired page after successful signup
            return HttpResponse("successfully created")
    else:
        return redirect('index')

    return render(request, 'signup.html')


def login_distributor(request):
    if request.user.is_authenticated:
        return redirect('order')
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
    if request.user.is_authenticated:
        distri= request.user.user_distributor
        orders=Order.objects.filter(distributor_name=distri).order_by('-order_date')
        main_itm_list=[]
        tickets = Ticket.objects.filter(user_distributor=distri).order_by('-id')
        products = Product.objects.all()
    else:
        return redirect('login')
    return render(request, 'order.html', {'distri':distri,'products': products, 'orders':orders,'tickets':tickets })


def admin_order_details(request):
    if request.user.is_superuser or request.user.is_staff:
        open_orders = Order.objects.filter(order_closed=False).order_by('-order_date')
        closed_orders = Order.objects.filter(order_closed=True).order_by('-order_date')
        context = {'open_orders': open_orders,'closed_orders':closed_orders}
        return render(request, 'admin_order_details.html', context)
    else:
        return redirect('login')

def close_order(request, order_id):
    if not request.user.is_superuser:
        return redirect('home')
    
    order = Order.objects.get(id=order_id)
    order.order_closed = True
    order.save()
    
    return redirect('admin_order_details')
    
def raise_ticket(request):
    
    if request.user.is_authenticated and request.user.user_distributor:
        if request.method == 'POST':
            subject = request.POST['subject']
            description = request.POST['description']
            ticket = Ticket.objects.create(user_distributor=request.user.user_distributor, subject=subject, description=description)
            return redirect('order')
    else:
        return redirect('login')
    return render(request, 'order.html')





def close_ticket(request, ticket_id):
    previous_url = request.META.get('HTTP_REFERER')
    if request.user.is_authenticated:
        ticket = Ticket.objects.get(id=ticket_id)
        ticket.closed = True
        ticket.closed_at = timezone.now()
        ticket.save()
        return redirect(previous_url)
    else:
        return redirect('login')


@user_passes_test(lambda user: user.is_superuser)
def ticket_list(request):
    if request.user.is_superuser:
        tickets = Ticket.objects.all().order_by('-id')
    else:
        return redirect('index')
    return render(request, 'ticket_admin.html', {'tickets': tickets})


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


def logoutUser(request):
    logout(request)
    return redirect('index')


