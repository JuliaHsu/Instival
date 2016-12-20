from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    userId = models.CharField(max_length=20,null=True,blank=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20,null=True,blank=True)
    
    def user(self) :
        return "User"
    
    
class Festival(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    date = models.DateTimeField(null=True)
    introduction = models.TextField(blank=True)
    def __str__(self):
        return self.name 
    
    def festival(self) :
        return "Festival"
    
    
class Profile(models.Model):
    user_id = models.ForeignKey(User)
    self_introduction = models.TextField(blank=True)
    past_post_group = models.TextField(blank=True)
    post_number = models.DecimalField(max_digits=10,decimal_places=0,default=0)
    like_id_group = models.TextField(blank=True)
    comment_id_group = models.TextField(blank=True)
    profile_picture = models.URLField(blank=True)
    
    def profile(self) :
        return "Profile"
    
class Post(models.Model):
    date = models.DateTimeField(default=timezone.now)
    festival_id = models.ForeignKey(Festival)
    location = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    user_id = models.ForeignKey(User)
    picture = models.URLField(null=True)
    like_number = models.DecimalField(max_digits=10,decimal_places=0,default=0)
    like_id_group = models.TextField(blank=True)
    comment_id_group = models.TextField(blank=True)
    
    def publish(self):
        self.date = timezone.now()
        self.save()
   
   

      
class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments')
    user_id = models.ForeignKey(User)
    content = models.TextField()
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()



    def __str__(self):
        return self.content
    
  