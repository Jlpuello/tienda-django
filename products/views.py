from django.shortcuts import render

from django.db.models import Q
from products.models import Products
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



class ProductListView(ListView):
    
    template_name = "index.html"
    queryset = Products.objects.all().order_by('-id')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = 'Listado de Productos' 
        
        return context


class ProductDetail(DetailView):
    model = Products
    template_name='products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context) 
        
        return context

class ProductSearchView(ListView):
    template_name= 'products/search.html'

    def get_queryset(self):
        filters = Q(title__icontains=self.query()) | Q(category__title__icontains=self.query())
        return Products.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q') 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query() 
        context['count'] = context['products_list'].count()
        
        return context