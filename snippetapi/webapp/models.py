from django.db import models
from django.contrib.auth.models import User, UserManager
# Create your models here.


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    title = models.TextField(unique=True)

class Snippet(models.Model):
    snip_id = models.AutoField(primary_key=True)
    snippet = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    created_user_id = models.TextField()
    tag = models.ForeignKey(Tag, models.CASCADE, related_name='snippets')
    title = models.TextField()

    class Meta:
        ordering = ['time_stamp']
