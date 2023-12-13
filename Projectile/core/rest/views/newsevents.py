from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from ...models import NewsEvents, NewsEventsFile

from ..serializers import newsevents

from ..permissions import common


class NewsEventsList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = NewsEvents.objects.filter(status="Active")
    serializer_class = newsevents.NewsEventsListSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields =  ['headline', 'publish_date']
    ordering = ['-publish_date']

   


class NewsEventsCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = NewsEvents.objects.filter(
        status="Active")
    serializer_class =  newsevents.NewsEventsListSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields =  ['headline', 'publish_date']

    def post(self, request, format=None, **kwargs):
        serializer = newsevents.NewsEventsOnboardingSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)




class NewsEventsRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = NewsEvents.objects.all()
    serializer_class = newsevents.UpdateNewsEventsSerializer
    lookup_field = 'uid'



class NewsEventsFileCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = NewsEventsFile.objects.filter(
        news_events__status="Active").select_related('news_events')
    serializer_class =  newsevents.NewsEventsFileListSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields =  ['news_events__headline', 'news_events__publish_date']

    def post(self, request, format=None, **kwargs):
        serializer = newsevents.NewsEventsFileOnboardingSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class FileRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = NewsEventsFile.objects.all()
    serializer_class = newsevents.FileSerializer
    lookup_field = 'uid'
    