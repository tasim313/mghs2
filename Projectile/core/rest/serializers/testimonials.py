from rest_framework import serializers 

from versatileimagefield.serializers import VersatileImageFieldSerializer

from ...models import TESTIMONIALS
from ...utils import get_testimonial_image
from ...choice import UserStatus

import logging

logger = logging.getLogger(__name__)



class TestimonialListCreateSerializers(serializers.ModelSerializer):
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
        model = TESTIMONIALS
        fields = (
            'uid',
            'name',
            'designation',
            'comment',
            'image'
        )



class TestimonialsOnboardingSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=300, trim_whitespace=True)
    designation = serializers.CharField(max_length=None, trim_whitespace=True)
    comment = serializers.CharField(max_length=None, trim_whitespace=True)
    image = serializers.ImageField(max_length=None,
                                     allow_empty_file=False,
                                     use_url=get_testimonial_image,
                                     required=False)
    
    class Meta:
        fields = (
            'uid',
            'name',
            'designation',
            'comment',
            'image',
        )


    def create(self, validated_data, *args, **kwargs):

        request = self.context['request']
        user = request.user
        name = validated_data['name']
        comment = validated_data['comment']
        image = validated_data['image']
        designation = validated_data['designation']
        
        testimonial = TESTIMONIALS.objects.create(
                        name=name,
                        designation = designation,
                        comment = comment,
                        image=image,
                        user_created=user,
                        status=UserStatus.Active,
                        ) 
       
        logger.debug(f"Created new testimonials: {testimonial}")

        return testimonial


class TestimonialsListSerializers(serializers.ModelSerializer):
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
        model = TESTIMONIALS
        fields = (
            'uid',
            'name',
            'designation',
            'comment',
            'image',
            'created_date',
            'updated_date',
            'status',
            'user_created',
            'user_updated',
        )