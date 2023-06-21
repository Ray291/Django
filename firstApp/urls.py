from django.urls import path, re_path
from firstApp import views

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('products/', views.products),
    path('product/<int:product_id>', views.product),
    re_path(r'^read-year/(?P<year>[0-9]{4})/$', views.read_year),
    path('index-2/', views.index_2)
]