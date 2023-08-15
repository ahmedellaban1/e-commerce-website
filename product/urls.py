from django.urls import path
from .views import home_page, shop_page, product_details
app_name = 'product'
urlpatterns = [
    path('', home_page, name='home-page'),
    path('<int:id><str:slug>', product_details, name='product_details'),
    path('shop', shop_page, name='shop'),

]