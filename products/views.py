from django.shortcuts import render
from products.api.serializers import ProductSerializer
from products.models import Product
from rest_framework import generics
from products.api.helpers import ProductsResultsSetPagination


class ProductViewSet(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductsResultsSetPagination
