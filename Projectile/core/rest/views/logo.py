from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ...models import LogoFile

from ..serializers import logo

from ...pagination import StandardResultsSetPagination

from ..permissions import common



class LogoAPIView(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = LogoFile.objects.filter(status="Active")
    serializer_class = logo.LogoListCreateSerializers




class LogoList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    pagination_class = StandardResultsSetPagination
    queryset = LogoFile.objects.filter(status="Active")
    serializer_class = logo.LogoListCreateSerializers

    def post(self, request, format=None, **kwargs):
        serializer = logo.LogoOnboardingSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    



class LogoRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    pagination_class = StandardResultsSetPagination
    queryset = LogoFile.objects.all()
    serializer_class = logo.LogoUpdateSerializers
    lookup_field = 'uid'
