from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ...models import ServiceDetails
from ..serializers import service_details



class ServiceDetailsList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = ServiceDetails.objects.filter(status="Active")
    serializer_class = service_details.ServiceDetailsSerializer

    def get_queryset(self):
        uid = self.kwargs.get("uid", None)
        return self.queryset.filter(service_info__uid=uid)
    

    
class ServiceDetailsRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ServiceDetails.objects.all()
    serializer_class = service_details.ServiceDetailsUpdateSerializer
    lookup_field = 'uid'




class ServiceDetailsCreate(generics.CreateAPIView):
 
    permission_classes = [IsAuthenticated]
    queryset = ServiceDetails.objects.all()
    serializer_class =  service_details.ServiceDetailsCreateSerializer

    def post(self, request, format=None, **kwargs):
        serializer = service_details.ServiceDetailsCreateSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_queryset(self):
        uid = self.kwargs.get("uid", None)
        return self.queryset.filter(service_info__uid=uid)