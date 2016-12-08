from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    passward = models.CharField(max_length=20)
    
class Festival(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    date = models.DateTimeField
    introduction = models.TextField(blank=True)
    
class Profile(models.Model):
    user_id = models.ForeignKey(User)
    self_introduction = models.TextField(blank=True)
    past_post = models.TextField(blank=True)
    post_number = models.DecimalField(max_digits=10,decimal_places=0,default=0)
    like_id = models.TextField(blank=True)
    comment_id = models.TextField(blank=True)
    profile_picture = models.URLField(blank=True)
    
class Post(models.Model):
    date = models.DateTimeField
    festival_id = models.ForeignKey(Festival)
    location = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    user_id = models.ForeignKey(User)
    picture = models.URLField
    like_number = models.DecimalField(max_digits=10,decimal_places=0,default=0)
    like_id = models.TextField(blank=True)
    comment_id = models.TextField(blank=True)
        
class Comment(models.Model):
    post_id = models.ForeignKey(Post)
    user_id = models.ForeignKey(User)
    content = models.TextField