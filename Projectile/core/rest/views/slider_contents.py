from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from ...models import HomeSliderContent, HomeSliderContentFile

from ..serializers import slider_content

from ...pagination import StandardResultsSetPagination

from ..permissions import common


class HomeSliderContentList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = HomeSliderContentFile.objects.filter(status="Active").select_related('home_content')
    serializer_class = slider_content.SliderContentFileListSerializer


class HomeSliderContentCreate(generics.ListCreateAPIView):
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = HomeSliderContent.objects.filter(
        status="Active")
    serializer_class =  slider_content.SliderContentListSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields =  ['title']

    def post(self, request, format=None, **kwargs):
        serializer = slider_content.SliderContentOnboardingSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)




class HomeSliderContentRetrieveUpdate(generics.RetrieveUpdateAPIView):
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = HomeSliderContent.objects.all()
    serializer_class = slider_content.UpdateSliderContentSerializer
    lookup_field = 'uid'



class HomeSliderContentFileCreate(generics.CreateAPIView):
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = HomeSliderContentFile.objects.filter(
        status="Active").select_related('home_content')
    serializer_class =  slider_content.SliderContentFileOnboardingSerializer

    def get_queryset(self):
        uid = self.kwargs.get("uid", None)
        return self.queryset.filter(home_content__uid=uid)



class HomeSliderContentFileRetrieveUpdate(generics.RetrieveUpdateAPIView):
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
    queryset = HomeSliderContentFile.objects.all()
    serializer_class = slider_content.FileSerializer
    lookup_field = 'uid'
