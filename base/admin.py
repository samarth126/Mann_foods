from django.contrib import admin


# Register your models here.
from .models import *


admin.site.register(User_distributor)
admin.site.register(Distributor_Applicants)
admin.site.register(Blogs)
admin.site.register(gallery)
admin.site.register(Ticket)
admin.site.register(About)
admin.site.register(Offers)




admin.site.register(categorie)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # Set the number of empty forms to display (0 for none)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    # actions = [generate_pdf]
