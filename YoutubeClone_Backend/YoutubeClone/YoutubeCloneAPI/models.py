from django.db import models
from django.db import models
# Create your models here.
class Comment(models.Model):
    comment = models.CharField(max_length=500)
    likes = models.IntegerField(default=0 )
    dislikes = models.IntegerField(default=0)
    video = models.CharField(max_length=50)

class Reply(models.Model):
    reply = models.CharField(max_length=500)
    comment = models.ForeignKey(Comment, null=True, on_delete=models.CASCADE)