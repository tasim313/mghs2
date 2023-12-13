from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from ...models import ProductDetails
from ..serializers import productdetails
# from ..permissions import common


class ProductDetailsList(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = ProductDetails.objects.filter(status="Active")
    serializer_class = productdetails.ProductDetailsSerializer

    def get_queryset(self):
        uid = self.kwargs.get("uid", None)
        return self.queryset.filter(products_info__uid=uid)
    

    
class ProductDetailsRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProductDetails.objects.all()
    serializer_class = productdetails.ProductDetailsUpdateSerializer
    lookup_field = 'uid'





class ProductDetailsFileCreate(generics.CreateAPIView):
 
    permission_classes = [IsAuthenticated]
    queryset = ProductDetails.objects.all()
    serializer_class =  productdetails.ProductDetailsCreateSerializer

    def post(self, request, format=None, **kwargs):
        serializer = productdetails.ProductDetailsCreateSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_queryset(self):
        uid = self.kwargs.get("uid", None)
        return self.queryset.filter(products_info__uid=uid)



class ProductDetailsListUsingSlug(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = ProductDetails.objects.filter(status="Active")
    serializer_class = productdetails.ProductDetailsSerializer

    def get_queryset(self):
        slug = self.kwargs.get("slug", None)
        return self.queryset.filter(products_info__slug=slug)