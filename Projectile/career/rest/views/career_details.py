from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from ...models import CareerDetails
from ..serializers import career_details




class CareerDetailsCreate(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    queryset = CareerDetails.objects.filter(
        status="Active")
    serializer_class =  career_details.CareerDetailCreateSerializer


    def post(self, request, format=None, **kwargs):
        serializer = career_details.CareerDetailCreateSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CareerDetailsList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = CareerDetails.objects.filter(status="Active")
    serializer_class = career_details.CareerDetailsListSerializer

    def get_queryset(self):
        uid = self.kwargs.get("uid", None)
        return self.queryset.filter(career_info__uid=uid)


class CareerDetailsRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CareerDetails.objects.all()
    serializer_class = career_details. CareerDetailsUpdateSerializer
    lookup_field = 'uid'