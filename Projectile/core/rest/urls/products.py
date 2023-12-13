from django.urls import path
from core.rest.views import products

urlpatterns = [
    path('', 
         products.ProductCreate.as_view(),
         name='product-list-create'),
    path('<uuid:uid>/',
         products.ProductRetrieveUpdate.as_view(),
         name='product-update'),
    path('list/', 
         products.ProductList.as_view(),
         name='products-list'),
]