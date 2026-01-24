from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('',views.catalog,name='catalog'),
    path("variant/<int:product_id>/", views.get_variant, name="get_variant"),
    path('product/<slug:product_slug>/',views.product_detail,name='product_detail'),
]
