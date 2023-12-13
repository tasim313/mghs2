from rest_framework import serializers 

from phonenumber_field.serializerfields import PhoneNumberField
from versatileimagefield.serializers import VersatileImageFieldSerializer

from ...models import Clients
from ...utils import get_client_logo
from ...choice import UserStatus

import logging

logger = logging.getLogger(__name__)



class ClientsLogoListCreateSerializers(serializers.ModelSerializer):
    logo = VersatileImageFieldSerializer(
        sizes=[
            ("original", "url"),
            ("at1024", "crop__1024x1024"),
            ("at512", "crop__512x512"),
            ("at256", "crop__256x256"),
        ],
        required=False,
    )

    class Meta:
        model = Clients
        fields = (
            'logo',
            'name',
        )



class ClientsOnboardingSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=300, trim_whitespace=True)
    head_office = serializers.CharField(max_length=None, trim_whitespace=True)
    email = serializers.EmailField()
    Phone = PhoneNumberField()
    logo = serializers.ImageField(max_length=None,
                                     allow_empty_file=False,
                                     use_url=get_client_logo,
                                     required=False)
    
    class Meta:
        fields = (
            'name',
            'head_office',
            'email',
            'Phone',
            'logo',
        )


    def create(self, validated_data, *args, **kwargs):

        request = self.context['request']
        user = request.user
        name = validated_data['name']
        head_office = validated_data['head_office']
        email = validated_data['email']
        Phone = validated_data['Phone']
        logo = validated_data['logo']
        
        clients = Clients.objects.create(
                        name=name,
                        head_office = head_office,
                        email = email,
                        Phone=Phone,
                        logo = logo,
                        user_created=user,
                        status=UserStatus.Active,
                        ) 
       
        logger.debug(f"Created new clients: {clients}")

        return clients


class ClientListSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Clients
        fields = (
            'uid',
            'logo',
            'name',
            'head_office',
            'email',
            'Phone',
            'slug',
            'created_date',
            'updated_date',
            'status',
            'user_created',
            'user_updated',
        )