from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User_distributor)
admin.site.register(Distributor_Applicants)
admin.site.register(Blogs)

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
