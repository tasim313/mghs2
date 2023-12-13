from rest_framework import serializers 
from versatileimagefield.serializers import VersatileImageFieldSerializer


from ...models import(
    CaseStudyDetails
)

from ...helpers import (
    get_case_study_instance,
    get_case_study_title_instance
)

from ...utils import (
    get_case_study_details_image
)


from core.choice import UserStatus

import logging

logger = logging.getLogger(__name__)


class CaseStudyDetailsOnOnboardingSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format='hex_verbose')
    introduction = serializers.CharField(max_length=None, trim_whitespace=True)
    challenges_goals = serializers.CharField(max_length=None, trim_whitespace=True)
    result = serializers.CharField(max_length=None, trim_whitespace=True)
    image = serializers.ImageField(max_length=None,
                                   allow_empty_file=False,
                                   use_url=get_case_study_details_image,
                                   required=False)
    challenges_image = serializers.ImageField(max_length=None,
                                   allow_empty_file=False,
                                   use_url=get_case_study_details_image,
                                   required=False)
    
    class Meta:
        fields = ('introduction', 'challenges_goals', 'result', 'image', 'challenges_image')
    
    
    def create(self, validated_data, *args, **kwargs):

        request = self.context['request']
        user = request.user
        
        uid = validated_data['uid']
        introduction = validated_data['introduction']
        challenges_goals = validated_data['challenges_goals']
        result = validated_data['result']
        image = validated_data['image']
        challenges_image = validated_data['challenges_image']

        case_study = get_case_study_instance(uid)
        title = get_case_study_title_instance(uid)
        
        case_study_details = CaseStudyDetails.objects.create(
            case_study_id = case_study,
            title = title,
            introduction=introduction,
            challenges_goals = challenges_goals,
            result = result,
            image=image,
            challenges_image = challenges_image,
            user_created=user,
            status=UserStatus.Active 
                        
            ) 
       
        logger.debug(f"Created : {case_study_details}")

        return case_study_details




class CaseStudyDetailsListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CaseStudyDetails
        fields = (
            'uid',
            'title',
            'introduction',
            'challenges_goals',
            'result',
            'image',
            'challenges_image',
        )



class UpdateCaseStudyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudyDetails
        fields = (
            'uid',
            'title',
            'introduction',
            'challenges_goals',
            'result',
            'image',
            'challenges_image',
            'status',
            'updated_date',
            'user_updated'
        )
