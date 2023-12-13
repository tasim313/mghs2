from rest_framework import serializers 

from versatileimagefield.serializers import VersatileImageFieldSerializer

from ...models import HomeSliderContent, HomeSliderContentFile

from ...choice import  UserStatus
from ...utils import get_home_slider_content_image
from ...helpers import get_home_slider_content_instance

import logging

logger = logging.getLogger(__name__)



class SliderContentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomeSliderContent
        fields = (
            'uid',
            'slug',
            'title',
            'description',
            'created_date',
            'updated_date',
            'status',
            'user_created',
            'user_updated'
        )


class SliderContentFileListSerializer(serializers.ModelSerializer):

    home_content = SliderContentListSerializer(required=False, read_only=True)
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
        model = HomeSliderContentFile
        fields = (
            'home_content',
            'uid',
            'image'
        )


class SliderContentOnboardingSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format='hex_verbose', read_only=True)
    
    title = serializers.CharField(max_length=30,
                                  trim_whitespace=True)
    description = serializers.CharField(max_length=100,
                                        trim_whitespace=True)
    
    class Meta:
        fields = (
            'title',
            'description',
        )


    def create(self, validated_data, *args, **kwargs):

        request = self.context['request']
        user = request.user
        title = validated_data['title']
        description = validated_data['description']
        
        slider_content = HomeSliderContent.objects.create(
                        title = title,
                        description = description,
                        user_created=user,
                        status=UserStatus.Active) 
       
        logger.debug(f"Created Home Page Slider Content: {slider_content}")

        return slider_content


class SliderContentFileOnboardingSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format='hex_verbose')
    image = serializers.ImageField(max_length=None,
                                     allow_empty_file=False,
                                     use_url=get_home_slider_content_image,
                                     required=False)

    
    class Meta:
        fields = (
            'uid',
            'image',
        )

    def create(self, validated_data, *args, **kwargs):

        request = self.context['request']
        user = request.user
        uid = validated_data['uid']
        image = validated_data['image']
        home_content = get_home_slider_content_instance(uid)

        file_obj = HomeSliderContentFile.objects.filter(home_content__uid=uid).select_related('home_content').count()

        if file_obj > 0:
            msg = 'Access denied: You Can not create new Image, Please update previous image or delete previous image'
            raise serializers.ValidationError(msg)
        
        slider_content_file = HomeSliderContentFile.objects.create(
                        home_content_id = home_content,
                        image = image,
                        user_created=user,
                        status=UserStatus.Active) 
       
        logger.debug(f"Created Home Page Slider Content File: {slider_content_file}")

        return slider_content_file
    


class UpdateSliderContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSliderContent
        fields = (
            'title',
            'description',
            'status',
            'updated_date',
            'user_updated'
        )



class FileSerializer(serializers.ModelSerializer):
    home_content = SliderContentListSerializer(required=False, read_only=True)
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
        model = HomeSliderContentFile
        fields = (
            'home_content',
            'uid',
            'image',
            'status',
            'updated_date',
            'user_updated'
        )