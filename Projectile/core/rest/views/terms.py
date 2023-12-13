from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ...models import TermsOfService

from ..serializers import terms

from ..permissions import common


class TermsOfServiceAPIView(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = TermsOfService.objects.filter(status="Active")
    serializer_class = terms.TermsOfServiceSerializers


class TermsOfServiceCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = TermsOfService.objects.filter(
        status="Active")
    serializer_class =  terms.TermsOfServiceSerializers

    def post(self, request, format=None, **kwargs):
        serializer = terms.TermsOfServiceSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class TermsOfServiceRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = TermsOfService.objects.all()
    serializer_class = terms.TermsOfServiceUpdateSerializers
    lookup_field = 'uid'