from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from ...models import WhyChooseUs, WhyChooseUsSubContent
from ..serializers import why_choose_us
# from ..permissions import common



class ContentList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()

    def get(self,request):
        choose_content = WhyChooseUs.objects.all()
       
    
        response = {
                "choose_content": why_choose_us.ContentListSerializer(
                                       choose_content,
                                       many=True).data
            }

        return Response(response)



class SubContentList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = WhyChooseUsSubContent.objects.filter(status="Active")
    serializer_class = why_choose_us.SubContentListSerializer



class WhyChooseUsCreate(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    queryset = WhyChooseUs.objects.filter(
        status="Active")
    serializer_class =  why_choose_us.WhyChooseUsListSerializer

    def post(self, request, format=None, **kwargs):
        serializer = why_choose_us.WhyChooseUsSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class WhyChooseUsRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WhyChooseUs.objects.all()
    serializer_class = why_choose_us.WhyChooseUsUpdateSerializer
    lookup_field = 'uid'
    



class WhyChooseUsSubContentCreate(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    queryset = WhyChooseUsSubContent.objects.filter(
        status="Active")
    serializer_class =  why_choose_us.WhyChooseUsSubContentCreateSerializer

    def post(self, request, format=None, **kwargs):
        serializer = why_choose_us.WhyChooseUsSubContentCreateSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    


class WhyChooseUsSubContentRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WhyChooseUsSubContent.objects.all()
    serializer_class = why_choose_us.WhyChooseUsSubContentUpdateSerializer
    lookup_field = 'uid'
