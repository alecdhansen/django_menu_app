from django.urls import path

from .views import MenuItemsAPIView

urlpatterns = [
    path("menuitems/", MenuItemsAPIView.as_view()),
]
