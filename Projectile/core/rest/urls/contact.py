from django.urls import path
from core.rest.views import contact

urlpatterns = [
    path('', contact.ContactList.as_view(), name='contact-list-create'),
    path('<uuid:uid>/', contact.ContactRetrieveUpdate.as_view(),
         name='contact-update'),
    path('list/', contact.ContactAPIView.as_view(), name='contact-list'),
]