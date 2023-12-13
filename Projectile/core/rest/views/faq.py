from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ...models import FrequentAskedQuestion, FrequentAskedQuestionSubContent

from ..serializers import faq

from ..permissions import common


class FrequentAskedQuestionList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = FrequentAskedQuestion.objects.filter(status="Active")
    serializer_class = faq.FrequentAskedQuestionSerializer



class FrequentAskedQuestionCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = FrequentAskedQuestion.objects.filter(
        status="Active")
    serializer_class =  faq.FrequentAskedQuestionListSerializer


    def post(self, request, format=None, **kwargs):
        serializer = faq.FrequentAskedQuestionCreateSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class FrequentAskedQuestionRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = FrequentAskedQuestion.objects.all()
    serializer_class = faq.UpdateFrequentAskedQuestionSerializer
    lookup_field = 'uid'


class FrequentAskedQuestionSubContentList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = FrequentAskedQuestionSubContent.objects.all()
    serializer_class = faq.FrequentAskedQuestionSubContentSerializer 



class FrequentAskedQuestionSubContentRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = FrequentAskedQuestionSubContent.objects.all()
    serializer_class = faq.UpdateFrequentAskedQuestionSubContentSerializer
    lookup_field = 'uid'


class FrequentAskedQuestionSubContentCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = FrequentAskedQuestionSubContent.objects.all()
    serializer_class = faq.FrequentAskedQuestionSubContentSerializer

    def post(self, request, format=None, **kwargs):
        serializer = faq.FrequentAskedQuestionSubContentSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def get_queryset(self):
        uid = self.kwargs.get("uid", None)
        return self.queryset.filter(frequent_asked_question_info__uid=uid)