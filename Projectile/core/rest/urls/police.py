from django.urls import path
from core.rest.views import police

urlpatterns = [
    path('list/',
         police.PrivacyPolicyAPIView.as_view(),
         name='police-list-create'),
    path('<uuid:uid>/', police.PrivacyPolicyRetrieveUpdate.as_view(),
         name='police-update'),
    path('', police.PrivacyPolicyCreateAPIView.as_view(), name='police-list'),
]