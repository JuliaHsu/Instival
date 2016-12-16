from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import Post,User
from .forms import PostForm
from .forms import CommentForm


# Create your views here.

def festival_each_post_gallery(request):
    posts=Post.objects.order_by('date')
    return render(request,'festival_each.html', {'posts':posts})
def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return  render(request, 'fullFestivalPic.html',{'post':post})
    else:
         form = CommentForm()
    context = {
            'post' : post,
            'form' : form,
        }
    return render(request, 'fullFestivalPic.html', context)
    # return render(request, 'fullFestivalPic.html',{'post':post})
    
# def upload(request):
#     if request.method == 'GET':
#         return render(request,"upload.html")
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             new_post_text = form.data.get("content")
#             Post.objects.create(user_id = 1 , festival_id = 1 ,location = "Taiwan",content = new_post_text,)
#             return redirect('views.post_detail', pk=post.pk) 
#         else:
#             form = PostForm(request.POST)
#             return render(request, 'upload.html', {'form': form})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return  render(request, 'fullFestivalPic.html',{'post':post})
    else:
         form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})