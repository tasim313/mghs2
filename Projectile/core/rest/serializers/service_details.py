from rest_framework import serializers 

from ...models import ServiceDetails 
from ...helpers import(
    get_service_instance,
    get_service_image_instance,
    get_service_short_description_instance,
    get_service_title_instance
)
from ...utils import(
    get_service_details_image
)
from  core.choice import UserStatus

import logging

logger = logging.getLogger(__name__)


class ServiceDetailsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = ServiceDetails  
        fields = (
            'uid',
            'title',
            'short_description',
            'long_description',
            'image',
            'short_description_image',
            )


class ServiceDetailsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDetails  
        fields = (
                'uid',
                'title',
                'short_description',
                'long_description',
                'image',
                'short_description_image',
                'status',
                'updated_date',
                'user_updated'
        )




class ServiceDetailsCreateSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format='hex_verbose')
    long_description = serializers.CharField(max_length=500000,
                                        trim_whitespace=True)
    
    short_description_image = serializers.ImageField(max_length=None,
                                   allow_empty_file=False,
                                   use_url=get_service_details_image,
                                   required=False)
    
    class Meta:
        fields = (
            'uid',
            'long_description',
            'short_description_image',
            )


    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        uid = validated_data['uid']
        long_description = validated_data['long_description']
        short_description_image = validated_data['short_description_image']
        
        service = get_service_instance(uid)
        title = get_service_title_instance(uid)
        short_description = get_service_short_description_instance(uid)
        image = get_service_image_instance(uid)

        service_details = ServiceDetails.objects.create(
                    service_info_id = service,
                    title=title,
                    short_description=short_description,
                    long_description = long_description,
                    image=image,
                    short_description_image = short_description_image,
                    user_created = user,
                    status=UserStatus.Active
                    ) 
        return service_details
    