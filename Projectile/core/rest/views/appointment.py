from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from ...models import Appointment

from ..serializers import appointment


class AppointmentList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Appointment.objects.all()
    serializer_class = appointment.AppointmentListSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields =  ['name', 'email', 'phone_number']


class AppointmentCreate(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = appointment.AppointmentCreateSerializer

    def post(self, request, format=None, **kwargs):
        serializer = appointment.AppointmentCreateSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AppointmentRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Appointment.objects.all()
    serializer_class = appointment.AppointmentSerializer
    lookup_field = 'uid'
