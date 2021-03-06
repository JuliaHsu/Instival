from django.contrib import admin

# Register your models here.
from .models import User
from .models import Festival
from .models import Profile
from .models import Post
from .models import Comment
from .models import Country
from .models import Festival_Country
class UserAdmin(admin.ModelAdmin):
    list_display = ('userId', 'name', 'email', 'password','profile_picture')
   


    
class FestivalAdmin(admin.ModelAdmin):
    list_display = ('name','date')
    
class Festival_CountryAdmin(admin.ModelAdmin):
    list_display =  ('id', 'location', 'festival','introduction')

   


 

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id','self_introduction', 'past_post_group', 'post_number', 'like_id_group', 
    'comment_id_group', 'profile_picture')
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('date', 'festival_id', 'location', 'content', 'user_id',
    'picture', 'like_number', 'like_id_group', 'comment_id_group')
   
    
class CommentAdmin(admin.ModelAdmin):

    list_display = ('post', 'user_id','content')
 
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    
admin.site.register(User,UserAdmin)
admin.site.register(Festival,FestivalAdmin)
admin.site.register(Festival_Country,Festival_CountryAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Country, CountryAdmin)

