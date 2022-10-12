from django.urls import path

from .views import MenuItemsAPIView, OrdersAPIView

urlpatterns = [
    path("menuitems/", MenuItemsAPIView.as_view()),
    path("orders/", OrdersAPIView.as_view()),
]
