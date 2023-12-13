from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ...models import LeaveMessage
from ..serializers import message


class LeaveMessageCreate(generics.CreateAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = LeaveMessage.objects.all()
    serializer_class =  message.LeaveMessageSerializer


class LeaveMessageList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = LeaveMessage.objects.all()
    serializer_class = message.LeaveMessageSerializer
    