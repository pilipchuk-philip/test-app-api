from orders.models import Order, OrderDetails
from rest_framework import viewsets
from rest_framework import serializers


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = ["product", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    order_details = OrderDetailSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "order_details",
        ]

    def create(self, validated_data):
        order = Order.objects.create(user=self.context["request"].user)
        [
            OrderDetails.objects.create(order=order, **order_details)
            for order_details in validated_data["order_details"]
        ]
        return order
