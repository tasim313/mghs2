from django.urls import path
from core.rest.views import service_details

urlpatterns = [
    
    path('update/<uuid:uid>/',
         service_details.ServiceDetailsRetrieveUpdate.as_view(),
         name='service-details-update'),
    path('<uuid:uid>/list/', 
         service_details.ServiceDetailsList.as_view(),
         name='service-details-list'),
    path('<uuid:service_info__uid>/create/', 
         service_details.ServiceDetailsCreate.as_view(),
         name='service-details-create'),
]