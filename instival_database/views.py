from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm
from .forms import CommentForm


# Create your views here.

def festival_each_post_gallery(request):
    posts=Post.objects.order_by('date')
    return render(request,'festival_each.html', {'posts':posts})
def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'fullFestivalPic.html',{'post':post})
    
def post_document(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.User
            post.festival_id = request.Festival
            post.date = timezone.now()
            post.location = "Taiwan"
            post.picture = "http://placehold.it/600x600"
            post.like_id_group = "123"
            post.comment_id_group = "123"
            post.like_number = 0
            post.save()
    return render(request, 'upload.html', {})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail.html', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'form': form})
    



