from django.db import models

# Create your models here.
class Music(models.Model):
    artist = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    date = models.DateTimeField()

    def summary(self):
        return self.body[:10]