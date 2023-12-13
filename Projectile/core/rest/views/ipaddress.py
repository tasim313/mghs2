from rest_framework import generics
from ...models import AppointmentUserAdditionalInformation
from core.rest.serializers import ipaddress
from ...pagination import StandardResultsSetPagination


class AppointmentUserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = ()
    authentication_classes = ()
    pagination_class = StandardResultsSetPagination
    queryset = AppointmentUserAdditionalInformation.objects.all()
    serializer_class = ipaddress.AppointmentAdditionalInfoSerializer
    lookup_field = 'id'