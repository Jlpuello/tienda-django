from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path ('search', views.ProductSearchView.as_view(), name='search'),
    path ('<slug:slug>', views.ProductDetail.as_view(), name='product'),
   
]
