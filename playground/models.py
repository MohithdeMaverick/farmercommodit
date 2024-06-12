from django.db import models

class Submission(models.Model):
    name = models.CharField(max_length=100)
    crop_type= models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
