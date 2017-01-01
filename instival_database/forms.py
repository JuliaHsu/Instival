from django import forms

from .models import Post,Comment,User

class PostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields=['content',]

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields=['user_id','content',]
        
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['name','email','password']
