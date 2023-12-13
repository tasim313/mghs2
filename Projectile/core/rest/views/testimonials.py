from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from ...models import TESTIMONIALS

from ..serializers import testimonials

from ..permissions import common


class TestimonialAPIView(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = TESTIMONIALS.objects.filter(status="Active")
    serializer_class = testimonials.TestimonialListCreateSerializers




class TestimonialCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = TESTIMONIALS.objects.filter(
        status="Active")
    serializer_class =  testimonials.TestimonialListCreateSerializers

    filter_backends = (filters.SearchFilter,)
    search_fields =  ['name',]

    def post(self, request, format=None, **kwargs):
        serializer = testimonials.TestimonialsOnboardingSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class TestimonialRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, common.CommonPermission]
    queryset = TESTIMONIALS.objects.all()
    serializer_class = testimonials.TestimonialsListSerializers
    lookup_field = 'uid'
