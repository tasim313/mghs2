from rest_framework import serializers 

from versatileimagefield.serializers import VersatileImageFieldSerializer

from ...models import CaseStudy

from ...choice import  UserStatus
from ...utils import get_case_study_image
from ..serializers import users

import logging

logger = logging.getLogger(__name__)


class CaseStudyListSerializer(serializers.ModelSerializer):
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
        model = CaseStudy
        fields = (
            'uid',
            'title',
            'subtitle',
            'image',
            'created_date',
            'updated_date',
            'status',
            'user_created',
            'user_updated',
        )


class CaseStudySerializer(serializers.ModelSerializer):
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
        model = CaseStudy
        fields = (
            'uid',
            'title',
            'subtitle',
            'image',
        )


class CaseStudyOnboardingSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format='hex_verbose', read_only=True)
    title = serializers.CharField(max_length=255, trim_whitespace=True)
    subtitle = serializers.CharField(max_length=100, trim_whitespace=True)
    image = serializers.ImageField(max_length=None,
                                   allow_empty_file=False,
                                   use_url=get_case_study_image,
                                   required=False)
    
    class Meta:
        fields = (
            'title',
            'subtitle',
            'image',
        )


    def create(self, validated_data, *args, **kwargs):

        request = self.context['request']
        user = request.user
        
        title = validated_data['title']
        subtitle = validated_data['subtitle']
        image = validated_data['image']
        
        case_study = CaseStudy.objects.create(
                        title = title,
                        subtitle = subtitle,
                        image=image,
                        user_created=user,
                        status=UserStatus.Active,
                        ) 
       
        logger.debug(f"Created new Case Studies: {case_study}")

        return case_study
    


class UpdateCaseStudiesSerializer(serializers.ModelSerializer):
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
        model = CaseStudy
        fields = (
            'uid',
            'title',
            'subtitle',
            'image',
            'status',
            'updated_date',
            'user_updated'
        )