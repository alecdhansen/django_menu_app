from rest_framework import serializers

from .models import MenuItem, Order


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ("id", "title", "tag", "description", "price", "img")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
