from django.shortcuts import render
from .models import Post
# Create your views here.

def festival_each_post_gallery(request):
    posts=Post.objects.order_by('date')
    return render(request,'fullFestivalPic.html', {'posts':posts})












