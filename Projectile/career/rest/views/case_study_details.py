from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from ...models import CaseStudyDetails
from ..serializers import case_study_details




class CaseStudyDetailsCreate(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    queryset = CaseStudyDetails.objects.filter(
        status="Active")
    serializer_class =  case_study_details.CaseStudyDetailsOnOnboardingSerializer


    def post(self, request, format=None, **kwargs):
        serializer = case_study_details.CaseStudyDetailsOnOnboardingSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def get_queryset(self):
        uid = self.kwargs.get("uid", None)
        return self.queryset.filter(case_study__uid=uid)


class CaseStudyDetailsList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = CaseStudyDetails.objects.filter(status="Active")
    serializer_class = case_study_details.CaseStudyDetailsListSerializer

    def get_queryset(self):
        uid = self.kwargs.get("uid", None)
        return self.queryset.filter(case_study__uid=uid)


class CaseStudyDetailsRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CaseStudyDetails.objects.all()
    serializer_class = case_study_details.UpdateCaseStudyDetailsSerializer
    lookup_field = 'uid'
