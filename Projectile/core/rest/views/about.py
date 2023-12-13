from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from ...models import About, AboutFile
from ..serializers import about
# from ..permissions import common


class AboutList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = About.objects.filter(status="Active")
    serializer_class = about.AboutSerializer



class AboutFileList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = AboutFile.objects.all().select_related('about')
    serializer_class = about.AboutFileListSerializer


class AboutCreate(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    queryset = About.objects.filter(
        status="Active")
    serializer_class =  about.AboutSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields =  ['title']

    def post(self, request, format=None, **kwargs):
        serializer = about.AboutCreateSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class AboutRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = About.objects.all()
    serializer_class = about.AboutUpdateSerializer
    lookup_field = 'uid'




class AboutFileRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AboutFile.objects.all()
    serializer_class = about.AboutFileUpdateSerializer
    lookup_field = 'uid'

