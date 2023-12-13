from rest_framework import serializers 
from ...models import  CareerDetails

from core.choice import UserStatus

from ...helpers import get_career_instance

import logging

logger = logging.getLogger(__name__)




class CareerDetailCreateSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format='hex_verbose')
    description  = serializers.CharField(max_length=None, trim_whitespace=True)
    responsibilities = serializers.CharField(max_length=None, trim_whitespace=True)
    qualifications = serializers.CharField(max_length=None, trim_whitespace=True)
    experience = serializers.CharField(max_length=None, trim_whitespace=True)
    benefits = serializers.CharField(max_length=None, trim_whitespace=True)
    
    class Meta:
        fields = (
            'uid',
            'description',
            'responsibilities',
            'qualifications',
            'experience',
            'benefits',
        )


    def create(self, validated_data, *args, **kwargs):

        uid = validated_data['uid']

        description = validated_data['description']
        responsibilities = validated_data['responsibilities']
        qualifications = validated_data['qualifications']
        experience = validated_data['experience']
        benefits = validated_data['benefits']

        career = get_career_instance(uid)

        career_obj = CareerDetails.objects.filter(career_info__uid=uid).select_related('case_study').count()

        if career_obj > 0:
            msg = 'Access denied: You Can not create new Career, Please update previous information or delete information'
            raise serializers.ValidationError(msg)
                
        career_details = CareerDetails.objects.create(
                career_info_id = career,
                description = description,
                responsibilities = responsibilities,
                qualifications = qualifications,
                experience = experience,
                benefits = benefits
                )
            
        
        logger.debug(f"Created Career Information: {career_details}")

        return career_details



class CareerDetailsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CareerDetails
        fields = (
            'uid',
            'title',
            'description',
            'responsibilities',
            'qualifications',
            'experience',
            'benefits'
        )


class CareerDetailsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerDetails
        fields = (
                'uid',
                'title',
                'description',
                'responsibilities',
                'qualifications',
                'experience',
                'benefits',
                'status',
                'updated_date',
                'user_updated'
        )