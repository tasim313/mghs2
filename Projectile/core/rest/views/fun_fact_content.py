from rest_framework import generics

from rest_framework.permissions import IsAuthenticated


from ...models import FunFactContent
from ..serializers import fun_fact_content



class FunFactContentList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = FunFactContent.objects.filter(status="Active")
    serializer_class =fun_fact_content.FunFactContentListSerializer



class FunFactContentRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FunFactContent.objects.all()
    serializer_class = fun_fact_content.FunFactContentSerializer
    lookup_field = 'uid'