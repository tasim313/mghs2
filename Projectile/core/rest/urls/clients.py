from django.urls import path
from core.rest.views import clients

urlpatterns = [
    path('',
         clients.ClientLogoAPIView.as_view(),
         name='client-logo-list-create'),
    path('<uuid:uid>/', clients.ClientsRetrieveUpdate.as_view(),
         name='clients-update'),
    path('create/', clients.ClientsCreate.as_view(), name='news-events-list'),
]