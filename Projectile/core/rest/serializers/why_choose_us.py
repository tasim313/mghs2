from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from ...models import WhyChooseUs, WhyChooseUsSubContent
from ...choice import UserStatus 
from ...utils import get_why_choose_us_content_image
from ...helpers import get_why_choose_content_instance
from ..serializers import users

import logging

logger = logging.getLogger(__name__)



class WhyChooseUsListSerializer(serializers.ModelSerializer):
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
        model = WhyChooseUs
        fields = (
            'uid',
            'headline',
            'short_description',
            'image',
            'created_date',
            'updated_date',
            'status',
            'user_created',
            'user_updated',
        )



class WhyChooseUsSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(format='hex_verbose', read_only=True)
    headline = serializers.CharField(
        max_length=255,
        trim_whitespace=True)
    short_description = serializers.CharField(max_length=500,
                                        trim_whitespace=True)
    image = serializers.ImageField(max_length=None,
                                     allow_empty_file=False,
                                     use_url=get_why_choose_us_content_image,
                                     required=False)
   
    class Meta:
        model = WhyChooseUs
        fields = (
            'uid',
            'headline',
            'short_description',
            'image',
            )


    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        headline = validated_data['headline']
        short_description = validated_data['short_description']
        image = validated_data['image']
        
        content_obj = WhyChooseUs.objects.all().count()

        if content_obj > 0:
            msg = 'Access denied: You Can not create new Content, Please update previous content or delete previous content'
            raise serializers.ValidationError(msg)
            
        else:
            content = WhyChooseUs.objects.create(
                        headline=headline,
                        short_description=short_description,
                        image=image,
                        user_created=user,
                        status=UserStatus.Active
                        )
            
        return content
    
    

class WhyChooseUsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseUs
        fields = (
                'uid',
                'headline',
                'short_description',
                'image',
                'status',
                'updated_date',
                'user_updated'
        )




class WhyChooseUsSubContentCreateSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format='hex_verbose')
    headline = serializers.CharField(
        max_length=255,
        trim_whitespace=True)
    short_description = serializers.CharField(max_length=500,
                                        trim_whitespace=True)
    class Meta:
        fields = ('uid', 'headline', 'short_description',)
    
    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        uid = validated_data['uid']
        instance = get_why_choose_content_instance(uid)
        headline = validated_data['headline']
        short_description = validated_data['short_description']

        content_file = WhyChooseUsSubContent.objects.create(
                    content_id=instance,
                    headline=headline,
                    short_description=short_description,
                    user_created=user,
                    status=UserStatus.Active) 
        return content_file




class WhyChooseUsSubContentListSerializer(serializers.ModelSerializer):
    user_created = users.UserSerializer(required=False, read_only=True)
    user_updated = users.UserSerializer(required=False, read_only=True)
    content = WhyChooseUsListSerializer(required=False, read_only=True)
    class Meta:
        model = WhyChooseUs
        fields = (
            'uid',
            'headline',
            'short_description',
            'created_date',
            'updated_date',
            'status',
            'content',
            'user_created',
            'user_updated',
        )



class WhyChooseUsSubContentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseUsSubContent
        fields = (
            'headline',
            'short_description',
            'updated_date',
            'status',
            'user_updated',
        )

class SubContentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseUsSubContent
        fields = (
            'headline',
            'short_description',
            )


class ContentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WhyChooseUs
        fields = (
            'uid',
            'headline',
            'short_description',
            'image',
            )