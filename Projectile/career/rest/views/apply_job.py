from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import filters


from ...models import EmployeeCandidate
from ..serializers import apply_job


class ApplyJobCreate(generics.CreateAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = EmployeeCandidate.objects.all()
    serializer_class =  apply_job.ApplyJobSerializer


    def post(self, request, format=None, **kwargs):
        serializer = apply_job.ApplyJobSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ApplyJobList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = EmployeeCandidate.objects.all()
    serializer_class = apply_job.CandidateListSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields =  ['job_category__designation', 'name', 'email', 'phone_number']



class ApplyJobListForSpecificJobCategory(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = EmployeeCandidate.objects.all()
    serializer_class = apply_job.CandidateListSerializer

    def get_queryset(self):
        uid = self.kwargs.get("uid", None)
        return self.queryset.filter(job_category__uid=uid)

    
