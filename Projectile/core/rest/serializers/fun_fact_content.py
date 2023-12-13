from rest_framework import serializers


from ...models import FunFactContent
from ...choice import UserStatus
from . import about
import logging

logger = logging.getLogger(__name__)



class FunFactContentSerializer(serializers.ModelSerializer):
    number_of_clients = serializers.CharField(max_length=50,
                                        trim_whitespace=True)
    delivered_products = serializers.CharField(max_length=50,
                                        trim_whitespace=True)
    winning_awards = serializers.CharField(max_length=50,
                                        trim_whitespace=True)
    
    class Meta:
        model = FunFactContent
        fields = (
            'number_of_clients',
            'delivered_products',
            'winning_awards',
            'user_updated',
            'status',
        )




class FunFactContentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunFactContent
        fields = (
            'uid',
            'years_of_experience',
            'number_of_clients',
            'delivered_products',
            'winning_awards'
        )