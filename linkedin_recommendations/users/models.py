from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Bio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)


    def __str__(self) -> str:
        return f"{self.id} - {self.name}"