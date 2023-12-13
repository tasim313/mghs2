from rest_framework import serializers 

from versatileimagefield.serializers import VersatileImageFieldSerializer

from ...models import Gallery

from ...choice import  UserStatus
from ...utils import get_gallery_image
from ..serializers import users

import logging

logger = logging.getLogger(__name__)





class GalleryListSerializer(serializers.ModelSerializer):
    user_created = users.UserSerializer(required=False, read_only=True)
    user_updated = users.UserSerializer(required=False, read_only=True)
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
        model = Gallery
        fields = (
            'uid',
            'image',
            'created_date',
            'updated_date',
            'status',
            'user_created',
            'user_updated',
        )


class GallerySerializer(serializers.ModelSerializer):
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
        model = Gallery
        fields = (
            "uid",
            'image',
        )


class GalleryOnboardingSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format='hex_verbose', read_only=True)
    image = serializers.ListField(
        child=serializers.ImageField(max_length=None,
                                     allow_empty_file=False,
                                     use_url=get_gallery_image,
                                     required=False))
    
    
    class Meta:
        fields = (
            'image',
        )


    def create(self, validated_data, *args, **kwargs):

        request = self.context['request']
        user = request.user
        
        images = validated_data['image']

        for image in images:
            gallery = Gallery.objects.create(
                image=image,
                user_created=user,
                status=UserStatus.Active,
                )
       
        logger.debug(f"Created new Image: {gallery}")

        return gallery
    


class UpdateGallerySerializer(serializers.ModelSerializer):
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
        model = Gallery
        fields = (
            'uid',
            'image',
            'status',
            'updated_date',
            'user_updated'
        )