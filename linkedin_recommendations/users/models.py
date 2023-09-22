from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
import uuid
from datetime import datetime

# Create your models here.
User = get_user_model()

class Bio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True, default='Blank-Profile-Picture.jpg')


    def __str__(self) -> str:
        return f"{self.user}"
    

class Recommendations(models.Model):
    # recommended_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default='') # current user
    recommended_by = models.CharField(max_length=100, null=True)
    recommended_user = models.CharField(max_length=100, null=True) # some other user
    recommendation = models.TextField(max_length=5000, null=True)
    rec_created_at = models.DateField(auto_now_add=True, null=True)


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    id = models.UUIDField(  primary_key= True, default= uuid.uuid4)
    post_img = models.ImageField(upload_to= 'posts', blank=True, null = True)
    caption = models.TextField()
    created_at  = models.DateTimeField(default = datetime.now)
    no_of_likes = models.IntegerField(default = 0)



class Follow(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.user
    
class Likes(models.Model):
    liked_by = models.CharField(max_length=100)
    post_id = models.CharField(max_length=200)
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('liked_by', 'post_id')


