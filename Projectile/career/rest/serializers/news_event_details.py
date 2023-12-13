from rest_framework import serializers 
from versatileimagefield.serializers import VersatileImageFieldSerializer

from ...models import(
    NewsEventsDetails,
)

from ...utils import  get_news_events_details_image
from ...helpers import(
    get_news_events_image,
    get_news_events_title,
    get_news_events_description,
    get_news_events_instance
)

from core.choice import UserStatus

import logging

logger = logging.getLogger(__name__)




class NewsEventsDetailsListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NewsEventsDetails
        fields = (
            'uid',
            'headline',
            'description',
            'publish_date',
            'image',
            'summarize_content_title',
            'summarize_content_description',
            'summarize_content_image',
            'quotes',
            'conclusion_content'
        )



class NewsEventsDetailsOnOnboardingSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format='hex_verbose')
    publish_date = serializers.DateTimeField()
    
    summarize_content_title = serializers.CharField(max_length=300, trim_whitespace=True)
    summarize_content_description = serializers.CharField(max_length=None, trim_whitespace=True)
    summarize_content_image = serializers.ImageField(max_length=None,
                                   allow_empty_file=False,
                                   use_url=get_news_events_details_image,
                                   required=False)
    quotes = serializers.CharField(max_length=None, trim_whitespace=True)
    conclusion_content = serializers.CharField(max_length=None, trim_whitespace=True)

    class Meta:
        fields = (
            'uid',
            'publish_date',
            'summarize_content_title',
            'summarize_content_description',
            'summarize_content_image',
            'quotes',
            'conclusion_content'
            )
    
    
    def create(self, validated_data, *args, **kwargs):

        request = self.context['request']
        user = request.user
        
        uid = validated_data['uid']
        publish_date = validated_data['publish_date']
        summarize_content_title = validated_data['summarize_content_title']
        summarize_content_description = validated_data['summarize_content_description']
        summarize_content_image = validated_data['summarize_content_image']
        quotes = validated_data['quotes']
        conclusion_content = validated_data['conclusion_content']

        new_events = get_news_events_instance(uid)
        headline = get_news_events_title(uid)
        description = get_news_events_description(uid)
        image = get_news_events_image(uid)

        news_obj = NewsEventsDetails.objects.filter(new_events__uid=uid).select_related('new_events').count()

        if news_obj > 0:
            msg = 'Access denied: You Can not create new News or Events, Please update previous News or Events or delete News or Events'
            raise serializers.ValidationError(msg)
        
        news_details_details = NewsEventsDetails.objects.create(
            new_events_id = new_events,
            headline=headline,
            description = description,
            image=image,
            publish_date = publish_date,
            summarize_content_title = summarize_content_title,
            summarize_content_description = summarize_content_description,
            summarize_content_image = summarize_content_image,
            quotes = quotes,
            conclusion_content = conclusion_content,
            user_created=user,
            status=UserStatus.Active            
            ) 
       
        logger.debug(f"Created : {news_details_details}")

        return news_details_details






class NewsEventsDetailsUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NewsEventsDetails
        fields = (
            'uid',
            'summarize_content_title',
            'summarize_content_description',
            'summarize_content_image',
            'quotes',
            'conclusion_content',
            'status',
            'updated_date',
            'user_updated'
        )