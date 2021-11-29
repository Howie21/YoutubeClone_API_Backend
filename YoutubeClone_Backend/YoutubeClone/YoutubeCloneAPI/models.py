from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Comment(models.Model):
    comment = models.CharField(max_length=500)
    likes = models.IntegerField(default=0 )
    dislikes = models.IntegerField(default=0)

class Reply(models.Model):
    comment = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    ForeignKey = models.ForeignKey(Comment, null=True, on_delete=models.CASCADE)