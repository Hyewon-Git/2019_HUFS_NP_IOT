from django.db import models

# Create your models here.
class Searchdb(models.Model):
    timedata = models.DateTimeField()
    distance = models.FloatField()

    class Meta:
        verbose_name_plural = "djapp"

    def __str__(self):
        return self.timedata