from rest_framework import serializers 
from  ...models import EmployeeCandidate
from phonenumber_field.serializerfields import PhoneNumberField

from ...helpers import get_career_instance
from ..serializers import career

import logging

logger = logging.getLogger(__name__)


class ApplyJobSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format='hex_verbose', write_only=True)
    name = serializers.CharField(max_length=500, trim_whitespace=True)
    email = serializers.EmailField()
    phone_number = PhoneNumberField()
    portfolio_link = serializers.URLField(max_length=200, min_length=None, allow_blank=False)
    linkedin_link = serializers.URLField(max_length=200, min_length=None, allow_blank=False)
    comment = serializers.CharField(max_length=None, trim_whitespace=True)
    curriculum_vitae = serializers.FileField(allow_null=True, allow_empty_file=True, required=False) 


    class Meta:
        fields = (
            'name',
            'email',
            'phone_number',
            'portfolio_link',
            'linkedin_link',
            'comment',
            'curriculum_vitae',
        )


    def create(self, validated_data, *args, **kwargs):

        uid = validated_data['uid']
        name = validated_data['name']
        email = validated_data['email']
        phone_number = validated_data['phone_number']
        portfolio_link = validated_data['portfolio_link']
        linkedin_link = validated_data['linkedin_link']
        comment = validated_data['comment']
        curriculum_vitae = validated_data['curriculum_vitae']

        job_category = get_career_instance(uid)
        
        candidate = EmployeeCandidate.objects.create(
                        name = name,
                        email = email,
                        phone_number = phone_number,
                        portfolio_link = portfolio_link,
                        linkedin_link = linkedin_link,
                        job_category_id = job_category,
                        comment = comment,
                        curriculum_vitae = curriculum_vitae,
                        ) 
       
        logger.debug(f"Created new candidate: {candidate}")

        return candidate



class CandidateListSerializer(serializers.ModelSerializer):
    job_category = career.CareerSerializer(required=False, read_only=True)
    class Meta:
        model = EmployeeCandidate
        fields = (
            'name',
            'email',
            'phone_number',
            'portfolio_link',
            'linkedin_link',
            'job_category',
            'comment',
            'created_date',
            'curriculum_vitae',
        )