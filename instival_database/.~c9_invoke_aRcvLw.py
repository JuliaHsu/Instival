from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    passward = models.CharField(max_length=20)
    
class Festival(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    date = models.CharField(max_length=10)
    introduction = models.CharField(max_length=100)
    
class Profile(models.Model):
    user_id = models.ForeignKey(User)
    self_introduction = models.CharField(max_length=100)
    past_post = models.DecimalField(max_digits=10,decimal_places=0)
    post_number = models.DecimalField(max_digits=10,decimal_places=0)
    prlike_id = models.ForeignKey(User)
    comment_id = models.DecimalField(max_digits=10,decimal_places=0)
    profile_picture = models.URLField(blank=True)
    
class Post(models.Model):
    date = models.CharField(max_length=10)
    festival_id = models.ForeignKey(Festival)
    location = models.CharField(max_length=20)
    content = models.TextField
    user_id = models.ForeignKey(User)
    picture = models.URLField(blank=True)
    like_number = models.DecimalField(max_digits=10,decimal_places=0)
    like_id = models.TextField
   # comment_id = models.ForeignKey(Comment)
        
class Comment(models.Model):
    post_id = models.ForeignKey(Post)
    user_id = models.ForeignKey(User)
    content = models.TextField