from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from ...models import Career, CareerDetails
from ..serializers import career


class CareerList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = Career.objects.filter(status="Active")
    serializer_class = career.CareerSerializer


class CareerCreate(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Career.objects.filter(
        status="Active")
    serializer_class =  career.CareerSerializer


    def post(self, request, format=None, **kwargs):
        serializer = career.CareerCreateSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class CareerRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Career.objects.all()
    serializer_class = career.CareerUpdateSerializer
    lookup_field = 'uid'
