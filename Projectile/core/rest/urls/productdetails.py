from django.urls import path
from core.rest.views import productdetails

urlpatterns = [
    
    path('update/<uuid:uid>/',
         productdetails.ProductDetailsRetrieveUpdate.as_view(),
         name='product-details-update'),
    path('<uuid:uid>/list/', 
         productdetails.ProductDetailsList.as_view(),
         name='product-details-list'),
    path('<uuid:products_info__uid>/create/', 
         productdetails.ProductDetailsFileCreate.as_view(),
         name='product-details-list'),
    path('<slug:slug>/list/', 
         productdetails.ProductDetailsListUsingSlug.as_view(),
         name='product_details_list'),
]  