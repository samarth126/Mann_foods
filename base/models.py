from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#distributor profile
class User_distributor(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    user_companyname=models.CharField(max_length=150, blank=False)
    user_mobile=models.CharField(max_length=12,blank=False)
    user_address=models.CharField(max_length=200, blank=False)
    user_created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

class Product(models.Model):

    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=8, decimal_places=2)


class Order(models.Model):
    distributor_name = models.ForeignKey(User_distributor, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


# Apply for distributer form
class Distributor_Applicants(models.Model):
    #desired are for agency
    applicant_state_name=models.CharField(max_length=100)
    applicant_district_name=models.CharField(max_length=100)
    applicant_tulka=models.CharField(max_length=100)
    #personal info
    personal_name=models.CharField(max_length=40)
    personal_age=models.IntegerField()
    personal_address=models.CharField(max_length=200)
    personal_pincode=models.CharField(max_length=7)
    personal_companyname=models.CharField(max_length=150)
    personal_mobile=models.CharField(max_length=12)
    personal_alt_mobile=models.CharField(max_length=12,blank=True)
    personal_telephone=models.CharField(max_length=12,blank=True)
    personal_email=models.EmailField(max_length=254)
    personal_educational_details=models.TextField()

    #partner info
    partner_name=models.CharField(max_length=40)
    partner_address=models.CharField(max_length=200)
    partner_pincode=models.CharField(max_length=7)
    partner_mobile=models.CharField(max_length=12)
    partner_alt_mobile=models.CharField(max_length=12,blank=True)
    partner_telephone=models.CharField(max_length=12,blank=True)
    partner_email=models.EmailField(max_length=254)
    
    #other info
    applicant_experience=models.TextField()
    applicant_storage_check=models.BooleanField()
    applicant_storage_info=models.IntegerField(null=True,blank=True)
    applicant_transport_check=models.BooleanField()
    applicant_transport_info=models.CharField(max_length=200,blank=True)
    applicant_invesment_capacity=models.CharField(max_length=200)
    
    def __str__(self):
        return self.personal_name

# blog model here
class Blogs(models.Model):
    blog_author = models.CharField(max_length=40)
    blog_heading = models.CharField(max_length=100)
    blog_text = models.TextField()
    blog_posted_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_heading