from rest_framework import serializers

from .models import MenuItem


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ("id", "title", "tag", "description", "price", "img")
