from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from ...models import Service
from ..serializers import services
# from ..permissions import common


class ServiceList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = Service.objects.filter(status="Active")
    serializer_class = services.ServiceSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields =  ['title']



class ServiceCreate(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Service.objects.filter(
        status="Active")
    serializer_class =  services.ServiceSerializer


    def post(self, request, format=None, **kwargs):
        serializer = services.ServiceCreateSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class ServiceRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Service.objects.all()
    serializer_class = services.ServiceUpdateSerializer
    lookup_field = 'uid'



class ServiceInfoList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = Service.objects.filter(status="Active")
    serializer_class = services.ServiceSerializerList
