from django.db import models

# Create your models here.
class animal(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    image=models.ImageField(upload_to='images/')