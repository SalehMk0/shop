from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register_shop',views.register_shop, name='register_shop'),
    path('create_shop',views.create_shop, name='create_shop'), 
    path('register_delivery',views.register_delivery, name='register_delivery'),
    path('register_client',views.register_client, name='register_client'),
    path('create_delivery', views.create_delivery, name='create_delivery'),
    path('404', views.custom_404_page, name='404'),
    
]
