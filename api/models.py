from django.db import models

# Create your models here.
class movieapi(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    detail=models.TextField()
    retting=models.CharField(max_length=10)
