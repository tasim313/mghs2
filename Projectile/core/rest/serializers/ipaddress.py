from rest_framework import serializers

from ...models import AppointmentUserAdditionalInformation


class AppointmentAdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentUserAdditionalInformation
        fields = (
            'appointment_user',
            'created_date',
            'ip_address',
            'browser',
            'operating_system',
            'online',
            'cookieEnabled',
            'user_agent',
        )