from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blogs/", views.blogs, name="blogs"),
    path("categories/", views.categories, name="categories"),
    path("products/<slug:slug>/", views.products, name="products"),
    path("blog_detail/", views.blog_detail, name="blog_detail"),
    path('order/', views.order, name="order"),
    path('place_order/', views.place_order, name="place_order")
    # path("", views.blog_detail, name="blog_detail"),
    # path("", views.blog_detail, name="blog_detail"),
]