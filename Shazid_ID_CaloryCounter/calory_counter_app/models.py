from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class userUpdate(models.Model):
    GENDER=[
        ("Female","Female"),
        ("Male","Male")]
    Name=models.CharField(max_length=20)
    age=models.FloatField()
    gender=models.CharField(max_length=10,choices=GENDER)
    height=models.FloatField()
    weight=models.FloatField()   
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.Name
