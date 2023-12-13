from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ...models import PrivacyPolicy

from ..serializers import police

from ..permissions import common


class PrivacyPolicyAPIView(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = PrivacyPolicy.objects.filter(status="Active")
    serializer_class = police.PrivacyPolicySerializers


class PrivacyPolicyCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = PrivacyPolicy.objects.filter(
        status="Active")
    serializer_class =  police.PrivacyPolicySerializers

    def post(self, request, format=None, **kwargs):
        serializer = police.PrivacyPolicySerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class PrivacyPolicyRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = PrivacyPolicy.objects.all()
    serializer_class = police.PrivacyPolicyUpdateSerializers
    lookup_field = 'uid'