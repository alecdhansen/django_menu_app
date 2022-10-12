from rest_framework import generics

from .models import MenuItem
from .serializers import BookSerializer

# Create your views here.
class MenuItemsAPIView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = BookSerializer
