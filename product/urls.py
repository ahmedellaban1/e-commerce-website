from django.urls import path
from .views import home_page, shop_page
app_name = 'product'
urlpatterns = [
    path('', home_page, name='home-page'),
    path('shop', shop_page, name='shop'),

]