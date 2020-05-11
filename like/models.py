from django.db import models

# Create your models here.


class Like(models.Models):
    uid = models.IntegerField()
    wid = models.IntegerField()
    created = models.DateTimeField()
