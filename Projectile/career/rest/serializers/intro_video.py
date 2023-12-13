from rest_framework import serializers

from ...models import IntroVideo
from core.choice import UserStatus

import logging

logger = logging.getLogger(__name__)


class IntroVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = IntroVideo
        fields = (
            'uid',
            'videoId',
        )



class IntroVideoCreateSerializer(serializers.ModelSerializer):
    videoId = serializers.CharField(
        max_length=500,
        trim_whitespace=True)
   
    class Meta:
        model = IntroVideo
        fields = (
            'videoId',
        )


    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        videoId = validated_data['videoId']
        video_obj = IntroVideo.objects.all().count()

        if video_obj > 0:
            msg = 'Access denied: You Can not create new Video ID, Please update previous information or delete previous data'
            raise serializers.ValidationError(msg)
            
        else:
            video = IntroVideo.objects.create(
                        videoId=videoId,
                        user_created=user,
                        status=UserStatus.Active
                        )
            
        return video
    
    


class IntroVideoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntroVideo
        fields = (
                'uid',
                'videoId',
                'status',
                'updated_date',
                'user_updated'
        )

