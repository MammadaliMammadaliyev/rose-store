from django.urls import path
from .views import (
    home,
    flower_api_view,
    product_api_view,
    basket_api_view,
    entourage_api_view,
    branch_api_view,
    package_api_view,
    houseplant_api_view,
    order_api_view,
    gift_api_view,
)

app_name = "products"

urlpatterns = [
    path("", home),
    path("flowers/", flower_api_view),
    path("products/", product_api_view),
    path("baskets/", basket_api_view),
    path("entourages/", entourage_api_view),
    path("branches/", branch_api_view),
    path("packages/", package_api_view),
    path("houseplants/", houseplant_api_view),
    path("orders/", order_api_view),
    path("gifts/", gift_api_view),
]