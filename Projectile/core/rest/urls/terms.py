from django.urls import path
from core.rest.views import terms

urlpatterns = [
    path('list/',
         terms.TermsOfServiceAPIView.as_view(),
         name='terms-list-create'),
    path('<uuid:uid>/', terms.TermsOfServiceRetrieveUpdate.as_view(),
         name='terms-update'),
    path('', terms.TermsOfServiceCreateAPIView.as_view(), name='terms-list'),
]