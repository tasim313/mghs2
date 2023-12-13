from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ...models import CaseStudy

from ..serializers import case_study

from ..permissions import common


class CaseStudiesList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = CaseStudy.objects.filter(status="Active")
    serializer_class = case_study.CaseStudySerializer



class CaseStudyCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = CaseStudy.objects.filter(
        status="Active")
    serializer_class =  case_study.CaseStudyListSerializer


    def post(self, request, format=None, **kwargs):
        serializer = case_study.CaseStudyOnboardingSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CaseStudiesRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = CaseStudy.objects.all()
    serializer_class = case_study.UpdateCaseStudiesSerializer
    lookup_field = 'uid'



# class NewsEventsFileCreate(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated, common.CommonPermission]
#     queryset = NewsEventsFile.objects.filter(
#         news_events__status="Active").select_related('news_events')
#     serializer_class =  newsevents.NewsEventsFileListSerializer

#     filter_backends = (filters.SearchFilter,)
#     search_fields =  ['news_events__headline', 'news_events__publish_date']

#     def post(self, request, format=None, **kwargs):
#         serializer = newsevents.NewsEventsFileOnboardingSerializer(
#             data=request.data,
#             context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# class FileRetrieveUpdate(generics.RetrieveUpdateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = NewsEventsFile.objects.all()
#     serializer_class = newsevents.FileSerializer
#     lookup_field = 'uid'
