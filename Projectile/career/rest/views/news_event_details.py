from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from ...models import NewsEventsDetails
from ..serializers import news_event_details



class NewsEventsDetailsList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = NewsEventsDetails.objects.filter(status="Active")
    serializer_class = news_event_details.NewsEventsDetailsListSerializer

    def get_queryset(self):
        uid = self.kwargs.get("uid", None)
        return self.queryset.filter(new_events__uid=uid)



class NewsEventsDetailsRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = NewsEventsDetails.objects.all()
    serializer_class = news_event_details.NewsEventsDetailsUpdateSerializer
    lookup_field = 'uid'

   


class NewsEventsDetailsCreate(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    queryset =NewsEventsDetails.objects.all()
    serializer_class =  news_event_details.NewsEventsDetailsOnOnboardingSerializer


    def post(self, request, format=None, **kwargs):
        serializer = news_event_details.NewsEventsDetailsOnOnboardingSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
