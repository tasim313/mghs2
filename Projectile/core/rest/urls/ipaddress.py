from django.urls import path
from core.rest.views import ipaddress

urlpatterns = [
    path('info/<id>/',
         ipaddress.AppointmentUserRetrieveUpdate.as_view(),
         name='info-list'), 
]