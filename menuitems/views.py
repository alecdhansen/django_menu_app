from rest_framework import generics

from .models import MenuItem, Order

from .serializers import BookSerializer, OrderSerializer

# Create your views here.
class MenuItemsAPIView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = BookSerializer


class OrdersAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
