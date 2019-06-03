from django.db import models

# Create your models here.
class Searchdb(models.Model):
    timedata = models.CharField(max_length=255)
    distance = models.IntegerField()

    class Meta:
        verbose_name_plural = "djapp"

    def __str__(self):
        return self.timedata