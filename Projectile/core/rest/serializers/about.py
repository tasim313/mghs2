from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from ...models import About , AboutFile
from ...choice import UserStatus


import logging

logger = logging.getLogger(__name__)


class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = (
            'uid',
            'title',
            'short_description',
            'support_description',
            'start_year',
            'years_of_experience',
            'vision',
            'mission',
        )



class AboutCreateSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(format='hex_verbose', read_only=True)
    title = serializers.CharField(
        max_length=200,
        trim_whitespace=True)
    short_description = serializers.CharField(max_length=1000,
                                        trim_whitespace=True)
    support_description = serializers.CharField(max_length=1000, trim_whitespace=True)
    start_year = serializers.DateField()
    vision = serializers.CharField(max_length=1000,
                                   trim_whitespace=True)
    mission = serializers.CharField(max_length=1000,
                                   trim_whitespace=True)
   
    class Meta:
        model = About
        fields = (
            'uid',
            'title',
            'short_description',
            'support_description',
            'start_year',
            'vision',
            'mission',
        )


    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        title = validated_data['title']
        short_description = validated_data['short_description']
        support_description = validated_data['support_description']
        start_year = validated_data['start_year']
        vision = validated_data['vision']
        mission = validated_data['mission']
        about_obj = About.objects.all().count()

        if about_obj > 0:
            msg = 'Access denied: You Can not create new About Information, Please update previous information or delete previous data'
            raise serializers.ValidationError(msg)
            
        else:
            about = About.objects.create(
                        title=title,
                        short_description=short_description,
                        support_description=support_description,
                        start_year=start_year,
                        vision=vision,
                        mission=mission,
                        user_created=user,
                        status=UserStatus.Active
                        )
            
        return about
    
    


class AboutUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = (
                'uid',
                'title',
                'short_description',
                'support_description',
                'start_year',
                'vision',
                'mission',
                'status',
                'updated_date',
                'user_updated'
        )



class AboutFileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutFile
        fields = ('image',)

    

class AboutFileListSerializer(serializers.ModelSerializer):
    about = AboutSerializer(required=False, read_only=True)
    class Meta:
        model = AboutFile
        fields = ('about', 'uid', 'image')