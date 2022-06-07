"""DOMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from orders import views as my_order
from django.contrib.auth import views as auth
from django.contrib.auth.decorators import login_required
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from .settings import DEBUG,MEDIA_URL,MEDIA_ROOT
from orders import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', my_order.index, name='home'),
    url(r'^orders$', my_order.index, name='home'),
    url(r'^order/(?P<order_id>\d+)/$', my_order.show, name='show'),
    url(r'^order/new/$', my_order.new, name='new'),
    url(r'^order/edit/(?P<order_id>\d+)/$', my_order.edit, name='edit'),
    url(r'^order/delete/(?P<order_id>\d+)/$', my_order.destroy, name='delete'),
    url(r'^products$', my_order.index_product, name='home_product'),
    url(r'^product/new/$', my_order.new_product, name='new_product'),
    url(r'^product/delete/(?P<product_id>\d+)/$', my_order.destroy_product, name='delete_product'),
    re_path(r'^users/login/$', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^users/logout/$',LoginView.as_view(template_name='login.html'), name='logout'),
    url(r'^signup/$', my_order.register_request, name="signup"),
    url(r'^users/change_password/$', auth_views.PasswordChangeView.as_view(template_name='change_password.html',success_url = '/'), name='change_password'),
]
if DEBUG:
     urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)