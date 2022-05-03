from rest_framework.serializers import ModelSerializer
from products.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Product
