from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(max_length=8)
    img = models.ImageField(upload_to="menuitems", null=True)

    def __str__(self):
        return self.title
