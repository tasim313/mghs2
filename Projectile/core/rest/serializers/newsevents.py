from rest_framework import serializers 

from versatileimagefield.serializers import VersatileImageFieldSerializer

from ...models import NewsEvents , NewsEventsFile

from ...choice import NewsEventsStatus, UserStatus
from ...utils import get_news_events_image, get_news_events_base_image
from ...helpers import get_news_events_instance
from ..serializers import users

import logging

logger = logging.getLogger(__name__)


class NewsEventsListSerializer(serializers.ModelSerializer):
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
        model = NewsEvents
        fields = (
            'uid',
            'choices',
            'slug',
            'headline',
            'description',
            'publish_date',
            'created_date',
            'updated_date',
            'status',
            'user_created',
            'user_updated',
            'image'
        )


class NewsEventsFileListSerializer(serializers.ModelSerializer):

    news_events = NewsEventsListSerializer(required=False, read_only=True)
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
        model = NewsEventsFile
        fields = (
            'news_events',
            'uid',
            'image'
        )


class NewsEventsOnboardingSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format='hex_verbose', read_only=True)
    choices = serializers.ChoiceField(
           choices = NewsEventsStatus.choices
    )
    headline = serializers.CharField(max_length=300, trim_whitespace=True)
    description = serializers.CharField(max_length=None, trim_whitespace=True)
    publish_date = serializers.DateTimeField()
    image = serializers.ImageField(max_length=None,
                                     allow_empty_file=False,
                                     use_url=get_news_events_base_image,
                                     required=False)
    
    class Meta:
        fields = (
            'choices',
            'headline',
            'description',
            'publish_date',
            'image',
        )


    def create(self, validated_data, *args, **kwargs):

        request = self.context['request']
        user = request.user
        choices = validated_data['choices']
        headline = validated_data['headline']
        description = validated_data['description']
        publish_date = validated_data['publish_date']
        image = validated_data['image']
        
        news_events = NewsEvents.objects.create(
                        choices=choices,
                        headline = headline,
                        description = description,
                        image=image,
                        publish_date = publish_date,
                        user_created=user,
                        status=UserStatus.Active,
                        ) 
       
        logger.debug(f"Created new news_or_events: {news_events}")

        return news_events


class NewsEventsFileOnboardingSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format='hex_verbose')
    image = serializers.ListField(
        child=serializers.ImageField(max_length=None,
                                     allow_empty_file=False,
                                     use_url=get_news_events_image,
                                     required=False))
    
    class Meta:
        fields = (
            'uid',
            'image',
        )


    def create(self, validated_data, *args, **kwargs):

        uid = validated_data['uid']

        images = validated_data['image']

        news_events = get_news_events_instance(uid)
                
      
        for image in images:
            news_events_file = NewsEventsFile.objects.create(
                news_events_id=news_events,
                image=image
                )
            
        
        logger.debug(f"Created Image: {news_events_file}")

        return news_events_file
    


class UpdateNewsEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsEvents
        fields = (
            'choices',
            'headline',
            'description',
            'publish_date',
            'image',
            'status',
            'updated_date',
            'user_updated'
        )



class FileSerializer(serializers.ModelSerializer):
    news_events = NewsEventsListSerializer(required=False, read_only=True)
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
        model = NewsEventsFile
        fields = (
            'news_events',
            'uid',
            'image'
        )