from django.urls import path
from core.rest.views import services

urlpatterns = [
    path('', 
         services.ServiceCreate.as_view(),
         name='service-list-create'),
    path('<uuid:uid>/',
         services.ServiceRetrieveUpdate.as_view(),
         name='service-update'),
    path('list/', 
         services.ServiceList.as_view(),
         name='service-list'),
    path('info/', 
         services. ServiceInfoList.as_view(),
         name='service-info-list'),
]