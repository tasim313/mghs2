from rest_framework import serializers 

from ...models import TermsOfService
from ...choice import UserStatus

import logging

logger = logging.getLogger(__name__)



class TermsOfServiceSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = TermsOfService
        fields = (
            'uid',
            'title',
            'description',
        )



class TermsOfServiceSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=300, trim_whitespace=True)
    description = serializers.CharField(max_length=1000, trim_whitespace=True)
    
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
        
        police = TermsOfService.objects.create(
                        title=title,
                        description = description,
                        user_created=user,
                        status=UserStatus.Active,
                        ) 
       
        logger.debug(f"Created new police: {police}")

        return police


class TermsOfServiceUpdateSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = TermsOfService
        fields = (
            'uid',
            'title',
            'description',
            'updated_date',
            'status',
            'user_updated',
        )