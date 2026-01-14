from django.urls import path

from . import views


app_name = 'cart'

urlpatterns = [
    path('',views.cart_detail, name='cart_detail'),
    path('update/<int:variant_id>/', views.cart_update, name='cart_update'),

]