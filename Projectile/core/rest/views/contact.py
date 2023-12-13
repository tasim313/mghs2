from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from ...models import Contact

from ..serializers import contact

from ...pagination import StandardResultsSetPagination

from ..permissions import common



class ContactAPIView(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = Contact.objects.filter(status="Active")
    serializer_class = contact.ContactSerializer




class ContactList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    pagination_class = StandardResultsSetPagination
    queryset = Contact.objects.filter(status="Active")
    serializer_class = contact.ContactSerializer



class ContactRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    pagination_class = StandardResultsSetPagination
    queryset = Contact.objects.all()
    serializer_class = contact.ContactUpdateSerializer
    lookup_field = 'uid'
