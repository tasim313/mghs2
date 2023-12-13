from rest_framework import serializers 
from phonenumber_field.serializerfields import PhoneNumberField

from ...models import Appointment
from ..serializers import services
from ...helpers import get_service_instance
import logging

logger = logging.getLogger(__name__)

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = (
            'uid',
            'slug',
            'name',
            'email',
            'phone_number',
            'appointment_date',
            'message',
            'service',
        )


class AppointmentCreateSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format='hex_verbose', write_only=True)
    name = serializers.CharField(max_length=500, trim_whitespace=True)
    email = serializers.EmailField()
    phone_number = PhoneNumberField()
    appointment_date = serializers.DateTimeField(required=False)
    message = serializers.CharField(max_length=555, trim_whitespace=True)
    


    class Meta:
        fields = (
            'name',
            'email',
            'phone_number',
            'appointment_date',
            'message',
        )


    def create(self, validated_data, *args, **kwargs):

        uid = validated_data['uid']
        name = validated_data['name']
        email = validated_data['email']
        phone_number = validated_data['phone_number']
        appointment_date = validated_data['appointment_date']
        message = validated_data['message']
        service = get_service_instance(uid)
        
        appointment = Appointment.objects.create(
                        name = name,
                        email = email,
                        phone_number = phone_number,
                        appointment_date = appointment_date,
                        message = message,
                        service_id = service,
                        ) 
       
        logger.debug(f"Created new appointment: {appointment}")

        return appointment



class AppointmentListSerializer(serializers.ModelSerializer):
    service = services.ServiceSerializerList(required=False, read_only=True)
    class Meta:
        model = Appointment
        fields = (
            'uid',
            'name',
            'email',
            'phone_number',
            'appointment_date',
            'message',
            'service',
        )