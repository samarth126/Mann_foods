from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blogs/", views.blogs, name="blogs"),
    path("about/", views.about,name="about"),
    path("categories/", views.categories, name="categories"),
    path("products/<slug:slug>/", views.products, name="products"),
    path("products/", views.product_all, name="product_all"),
    path("blog_detail/<blog_id>/",views.blog_detail, name="blog_detail"),
    path("distributor_reg/", views.distributor_reg, name="distributor_reg"),
    path('order/', views.order, name="order"),
    path('place_order/', views.place_order, name="place_order"),
    path('signup/', views.signup_distributor, name="signup_distributor"),
    path('login/', views.login_distributor, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('form-success/', views.success, name="success"),
    # path("", views.blog_detail, name="blog_detail"),
    # path("", views.blog_detail, name="blog_detail"),
    path('ticket_list/', views.ticket_list, name='ticket_list'),
    path('raise-ticket/', views.raise_ticket, name='raise_ticket'),
    path('ticket/<int:ticket_id>/close/', views.close_ticket, name='close_ticket'),
    path('admin/order-details/', views.admin_order_details, name='admin_order_details'),
    path('admin/orders/close/<int:order_id>/', views.close_order, name='close_order'),
]