from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


from ...models import Clients

from ..serializers import clients

from ..permissions import common


class ClientLogoAPIView(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = Clients.objects.filter(status="Active")
    serializer_class = clients.ClientsLogoListCreateSerializers




class ClientsCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = Clients.objects.filter(
        status="Active")
    serializer_class =  clients.ClientListSerializers

    filter_backends = (filters.SearchFilter,)
    search_fields =  ['name',]

    def post(self, request, format=None, **kwargs):
        serializer = clients.ClientsOnboardingSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class ClientsRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = Clients.objects.all()
    serializer_class = clients.ClientListSerializers
    lookup_field = 'uid'
