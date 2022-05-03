from django.urls import path
from products.views import ProductViewSet


urlpatterns = [
    path("products/", ProductViewSet.as_view()),
]
