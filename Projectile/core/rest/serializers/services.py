from rest_framework import serializers 
from versatileimagefield.serializers import VersatileImageFieldSerializer
from ...models import Service 
from ...choice import UserStatus
from ...utils import get_service_image

import logging

logger = logging.getLogger(__name__)


class ServiceSerializer(serializers.ModelSerializer):

    image = VersatileImageFieldSerializer(
        sizes=[
            ("original", "url"),
            ("at1024", "crop__1024x1024"),
            ("at512", "crop__512x512"),
            ("at256", "crop__256x256"),
        ],
        required=False,
    )
   
    class Meta:
        model = Service
        fields = ('uid','title', 'short_description', 'image')



class ServiceCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=1000,
        trim_whitespace=True)
    short_description = serializers.CharField(max_length=500000,
                                        trim_whitespace=True)
    image = serializers.ImageField(max_length=None,
                                   allow_empty_file=False,
                                   use_url=get_service_image,
                                   required=False)
   
    class Meta:
        model = Service
        fields = ('uid','title', 'short_description', 'image')


    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        title = validated_data['title']
        short_description = validated_data['short_description']
        image = validated_data['image']
        service = Service.objects.create(
                    title=title,
                    short_description=short_description,
                    image=image,
                    user_created=user,
                    status=UserStatus.Active
                    ) 
        return service
    
    


class ServiceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'uid',
            'title',
            'short_description',
            'image',
            'status',
            'updated_date',
            'user_updated'
        )


class ServiceSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'uid',
            'title',
        )