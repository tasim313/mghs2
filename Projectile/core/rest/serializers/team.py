from rest_framework import serializers 

from versatileimagefield.serializers import VersatileImageFieldSerializer

from ...models import Team
from ...utils import get_team_image
from ...choice import UserStatus

import logging

logger = logging.getLogger(__name__)



class TeamListSerializers(serializers.ModelSerializer):
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
        model = Team
        fields = (
            'uid',
            'name',
            'designation',
            'image',
        )



class TeamOnboardingSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=300, trim_whitespace=True)
    designation = serializers.CharField(max_length=255, trim_whitespace=True)
    image = serializers.ImageField(max_length=None,
                                     allow_empty_file=False,
                                     use_url=get_team_image,
                                     required=False)
    
    class Meta:
        fields = (
            'name',
            'designation',
            'image',
        )


    def create(self, validated_data, *args, **kwargs):

        request = self.context['request']
        user = request.user
        name = validated_data['name']
        designation = validated_data['designation']
        image = validated_data['image']
        
        teams = Team.objects.create(
                        name=name,
                        designation = designation,
                        image = image,
                        user_created=user,
                        status=UserStatus.Active,
                        ) 
       
        logger.debug(f"Created new member: {teams}")

        return teams


class TeamUpdateSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Team
        fields = (
            'uid',
            'name',
            'designation',
            'image',
            'updated_date',
            'status',
            'user_updated',
        )