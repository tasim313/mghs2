from rest_framework import serializers 

from versatileimagefield.serializers import VersatileImageFieldSerializer

from ...models import LogoFile
from ...utils import get_website_logo_image

import logging

logger = logging.getLogger(__name__)


class LogoListCreateSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = LogoFile
        fields = (
            'uid',
            'image',
            'created_date',
            'status',
            'user_created'
        )




class LogoOnboardingSerializer(serializers.Serializer):

    image = serializers.ImageField(max_length=None,
                                     allow_empty_file=False,
                                     use_url=get_website_logo_image,
                                     required=False)
    
    
    class Meta:
        fields = (
            'image',
        )


    def create(self, validated_data, *args, **kwargs):

        request = self.context['request']
        user = request.user
        
        image = validated_data['image']

        logo_obj = LogoFile.objects.all().count()

        if logo_obj > 0:
            msg = 'Access denied: You Can not create new Logo, Please update previous Logo or delete previous Logo'
            raise serializers.ValidationError(msg)
        
        logo = LogoFile.objects.create(
                image=image,
                user_created=user,
                )
       
        logger.debug(f"Created new Image: {logo}")

        return logo



class LogoUpdateSerializers(serializers.ModelSerializer):
    

    class Meta:
        model = LogoFile
        fields = (
            'uid',
            'image',
            'updated_date',
            'status',
            'user_updated'
        )
