from django.db import models

# Create your models here.
class Directory(models.Model):
    name = models.CharField(max_length = 64)
    parent = models.ForeignKey("Directory", null = True)

    def __str__(self):
        return self.name