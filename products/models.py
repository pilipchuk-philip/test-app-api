from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120, verbose_name="Product Name")
    price = models.DecimalField(
        decimal_places=2, max_digits=10, verbose_name="Product price"
    )
    quantity_in_stock = models.PositiveIntegerField(verbose_name="Product quantity")

    def __str__(self):
        return self.name
