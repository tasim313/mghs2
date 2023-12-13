from django.urls import path
from core.rest.views import logo

urlpatterns = [
    path('',
         logo.LogoList.as_view(),
         name='logo-list-create'),
    path('<uuid:uid>/',
         logo.LogoRetrieveUpdate.as_view(),
         name='logo-update'),
    path('list/',
         logo.LogoAPIView.as_view(),
         name='contact-list'),
]