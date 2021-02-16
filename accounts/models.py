from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Posts(models.Model):
    userid = models.ForeignKey(User,on_delete= models.PROTECT)
    title = models.TextField()
    body = models.TextField()