from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register_shop',views.register_shop, name='register_shop'),
    path('create_shop',views.create_shop, name='create_shop'), 
]