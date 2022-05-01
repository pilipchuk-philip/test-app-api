from django.db import models
from django.conf import settings


class OrderDetails(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    # def post_save(self, *args, **kwargs):
        # !TODO for order details quantity delete product quantity
        # breakpoint()

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

