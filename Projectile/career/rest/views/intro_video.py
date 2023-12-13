from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from ...models import IntroVideo
from ..serializers import intro_video


class IntroVideoList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = IntroVideo.objects.filter(status="Active")
    serializer_class = intro_video.IntroVideoSerializer



class IntroVideoCreate(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    queryset = IntroVideo.objects.filter(
        status="Active")
    serializer_class =  intro_video.IntroVideoCreateSerializer

    def post(self, request, format=None, **kwargs):
        serializer = intro_video.IntroVideoCreateSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class IntroVideoRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = IntroVideo.objects.all()
    serializer_class = intro_video.IntroVideoUpdateSerializer
    lookup_field = 'uid'