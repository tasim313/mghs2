from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ...models import Gallery

from ..serializers import gallery

from ..permissions import common


class GalleryList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = Gallery.objects.filter(status="Active")
    serializer_class = gallery.GallerySerializer



class GalleryCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = Gallery.objects.filter(
        status="Active")
    serializer_class =  gallery.GalleryListSerializer


    def post(self, request, format=None, **kwargs):
        serializer = gallery.GalleryOnboardingSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class GalleryRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = Gallery.objects.all()
    serializer_class = gallery.UpdateGallerySerializer
    lookup_field = 'uid'