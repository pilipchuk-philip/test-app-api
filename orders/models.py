from django.db import models
from django.conf import settings
from django.core.exceptions import EmptyResultSet


class OrderDetails(models.Model):
    order = models.ForeignKey(
        "Order", on_delete=models.CASCADE, related_name="order_details"
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="order_details"
    )
    quantity = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        if self.product.quantity_in_stock >= self.quantity:
            self.product.quantity_in_stock = (
                self.product.quantity_in_stock - self.quantity
            )
            self.product.save()
            super().save(*args, **kwargs)
        else:
            raise EmptyResultSet("Products not enough in stock")


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders"
    )
