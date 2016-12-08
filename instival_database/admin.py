from django.contrib import admin

# Register your models here.
from .models import User
from .models import  Festival
from .models import Profile
from .models import Post
from .models import Comment
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'passward')
    
class FestivalAdmin(admin.ModelAdmin):
    list_display =  ('name', 'location', 'date', 'introduction')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id','self_introduction', 'past_post', 'post_number', 'like_id', 
    'comment_id', 'profile_picture')
class PostAdmin(admin.ModelAdmin):
    list_display = ('date', 'festival_id', 'location', 'content', 'user_id',
    'picture', 'like_number', 'like_id', 'comment_id')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'user_id','content')
    
admin.site.register(User,UserAdmin)
admin.site.register(Festival,FestivalAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)

