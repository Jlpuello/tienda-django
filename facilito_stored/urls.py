from django.contrib import admin
from django.urls import path
from django.urls import include
from .import views

from django.conf.urls.static import static
from django.conf import settings

from products.views import ProductListView
from products.views import ProductDetail

urlpatterns = [
    path('',ProductListView.as_view(), name='index'),
    path('usuarios/logout', views.logoutviews ,name='logout'),
    path('usuarios/login', views.loginviews ,name='login'),
    path('usuarios/registro', views.register ,name='register'),
    path('admin/', admin.site.urls),
    path('productos/',include('products.urls')),
    path('carrito/', include('carts.urls')),
    path('ordern/', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    