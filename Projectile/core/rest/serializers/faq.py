from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from ...models import FrequentAskedQuestion, FrequentAskedQuestionSubContent
from ...choice import UserStatus
from ...utils import get_faq_image
from ..serializers import users
from ...helpers import get_FrequentAskedQuestion_instance


import logging

logger = logging.getLogger(__name__)




class FrequentAskedQuestionCreateSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(format='hex_verbose', read_only=True)
    title = serializers.CharField(
        max_length=300,
        trim_whitespace=True)
    image = serializers.ImageField(max_length=None,
                                     allow_empty_file=False,
                                     use_url=get_faq_image,
                                     required=False)
   
    class Meta:
        model = FrequentAskedQuestion
        fields = (
            'uid',
            'title',
            'image',
        )


    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        title = validated_data['title']
        image = validated_data['image']
        faq_obj = FrequentAskedQuestion.objects.all().count()

        if faq_obj > 0:
            msg = 'Access denied: You Can not create new  Information, Please update previous information or delete previous data'
            raise serializers.ValidationError(msg)
            
        else:
            faq = FrequentAskedQuestion.objects.create(
                        title=title,
                        image=image,
                        user_created=user,
                        status=UserStatus.Active
                        )
            
        return faq



class FrequentAskedQuestionListSerializer(serializers.ModelSerializer):
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
        model = FrequentAskedQuestion
        fields = (
            'uid',
            'title',
            'image',
            'created_date',
            'updated_date',
            'status',
            'user_created',
            'user_updated',
        )


class FrequentAskedQuestionSerializer(serializers.ModelSerializer):
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
        model = FrequentAskedQuestion
        fields = (
            'uid',
            'title',
            'image',
        )


class UpdateFrequentAskedQuestionSerializer(serializers.ModelSerializer):
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
        model = FrequentAskedQuestion
        fields = (
            'uid',
            'title',
            'image',
            'status',
            'updated_date',
            'user_updated'
        )




class FrequentAskedQuestionSubContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequentAskedQuestionSubContent
        fields = (
            'uid',
            'question',
            'answer',
        )



class UpdateFrequentAskedQuestionSubContentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FrequentAskedQuestionSubContent
        fields = (
            'uid',
            'question',
            'answer',
        )


class FrequentAskedQuestionSubContentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequentAskedQuestionSubContent
        fields = (
            'frequent_asked_question_info',
            'question',
            'answer',
        )



class FrequentAskedQuestionSubContentSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format='hex_verbose')
    question = serializers.CharField(
                max_length=300,
                trim_whitespace=True)
    answer = serializers.CharField(
                max_length=300,
                trim_whitespace=True)
    class Meta:
        fields = (
            'uid',
            'question',
            'answer',
        )


    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        uid = validated_data['uid']
        question = validated_data['question']
        answer = validated_data['answer']
        faq_obj = get_FrequentAskedQuestion_instance(uid)

        faq_sub_content = FrequentAskedQuestionSubContent.objects.create(
                        frequent_asked_question_info_id = faq_obj,
                        question = question,
                        answer = answer,
                        user_created=user,
                        status=UserStatus.Active
                        )
            
        return faq_sub_content

