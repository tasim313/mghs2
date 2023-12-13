from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from ...models import Product
from ..serializers import products
# from ..permissions import common


class ProductList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = Product.objects.filter(status="Active")
    serializer_class = products.ProductSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields =  ['title']



class ProductCreate(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Product.objects.filter(
        status="Active")
    serializer_class =  products.ProductSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields =  ['title']

    def post(self, request, format=None, **kwargs):
        serializer = products.ProductCreateSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class ProductRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = products.ProductUpdateSerializer
    lookup_field = 'uid'