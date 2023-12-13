from rest_framework import serializers 
from  ...models import LeaveMessage
from phonenumber_field.serializerfields import PhoneNumberField

import logging

logger = logging.getLogger(__name__)

class LeaveMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveMessage
        fields=(
            'name',
            'email',
            'phone_number',
            'subject',
            'message',
            'created_date',
        )