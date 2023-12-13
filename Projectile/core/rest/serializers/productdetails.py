from rest_framework import serializers 
from ...models import ProductDetails 

from ...utils import get_product_details_image
from ...helpers import (
    get_product_instance,
    get_product_title_instance,
    get_product_short_description_instance,
    get_product_image_instance
    )
from ...choice import UserStatus

import logging

logger = logging.getLogger(__name__)


class ProductDetailsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = ProductDetails 
        fields = (
            'uid',
            'title',
            'short_description',
            'long_description',
            'key_Feature',
            'image',
            'short_description_image',
            'long_description_image',
            'key_Feature_image'
            )




class ProductDetailsCreateSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format='hex_verbose')
    long_description = serializers.CharField(max_length=500000,
                                        trim_whitespace=True)
    key_Feature = serializers.CharField(max_length=500000, trim_whitespace=True)
    short_description_image = serializers.ImageField(max_length=None,
                                   allow_empty_file=False,
                                   use_url=get_product_details_image,
                                   required=False)
    long_description_image = serializers.ImageField(max_length=None,
                                   allow_empty_file=False,
                                   use_url=get_product_details_image,
                                   required=False)
    key_Feature_image = serializers.ImageField(max_length=None,
                                   allow_empty_file=False,
                                   use_url=get_product_details_image,
                                   required=False)
   
    class Meta:
        fields = (
            'uid',
            'long_description',
            'key_Feature',
            'short_description_image',
            'long_description_image',
            'key_Feature_image'
            )


    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        uid = validated_data['uid']
        long_description = validated_data['long_description']
        key_Feature = validated_data['key_Feature']
        short_description_image = validated_data['short_description_image']
        long_description_image = validated_data['long_description_image']
        key_Feature_image = validated_data['key_Feature_image']
        product = get_product_instance(uid)
        title = get_product_title_instance(uid)
        short_description = get_product_short_description_instance(uid)
        image = get_product_image_instance(uid)

        product_details = ProductDetails.objects.create(
                    products_info_id = product,
                    title=title,
                    short_description=short_description,
                    long_description = long_description,
                    key_Feature = key_Feature,
                    image=image,
                    short_description_image = short_description_image,
                    long_description_image = long_description_image,
                    key_Feature_image = key_Feature_image,
                    user_created = user,
                    status=UserStatus.Active
                    ) 
        return product_details
    




class ProductDetailsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails 
        fields = (
                'uid',
                'title',
                'short_description',
                'long_description',
                'key_Feature',
                'image',
                'short_description_image',
                'long_description_image',
                'key_Feature_image',
                'status',
                'updated_date',
                'user_updated'
        )