from rest_framework import serializers 

from ...models import Career, CareerDetails


from core.choice import UserStatus

from ...helpers import get_career_instance


import logging

logger = logging.getLogger(__name__)


class CareerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Career
        fields = (
            'uid',
            'designation',
            'education',
            'experience',
            'deadline',
        )


class CareerCreateSerializer(serializers.ModelSerializer):
    designation = serializers.CharField(
        max_length=550,
        trim_whitespace=True)
    education = serializers.CharField(max_length=550,
                                        trim_whitespace=True)
    experience = serializers.CharField(max_length=550, trim_whitespace=True)
    deadline = serializers.DateField()
    
   
    class Meta:
        model = Career
        fields = (
            'uid',
            'designation',
            'education',
            'experience',
            'deadline',
        )


    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        designation = validated_data['designation']
        education = validated_data['education']
        experience = validated_data['experience']
        deadline = validated_data['deadline']
            
        career = Career.objects.create(
                        designation=designation,
                        education=education,
                        experience=experience,
                        deadline=deadline,
                        user_created=user,
                        status=UserStatus.Active
                        )
            
        return career 
    



class CareerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = (
                'uid',
                'designation',
                'education',
                'experience',
                'deadline',
                'status',
                'updated_date',
                'user_updated'
        )
