from django.db import models

# Create your models here.
class Comment(models.Model):
    comment = models.CharField(max_length=500)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    