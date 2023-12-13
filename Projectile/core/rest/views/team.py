from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ...models import Team

from ..serializers import team

from ..permissions import common


class TeamAPIView(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = Team.objects.filter(status="Active")
    serializer_class = team.TeamListSerializers


class TeamCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = Team.objects.filter(
        status="Active")
    serializer_class =  team.TeamListSerializers

    def post(self, request, format=None, **kwargs):
        serializer = team.TeamOnboardingSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class TeamRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = Team.objects.all()
    serializer_class = team.TeamUpdateSerializers
    lookup_field = 'uid'
