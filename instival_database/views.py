from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import Post,User,Festival
from .forms import PostForm
from .forms import CommentForm
from datetime import datetime, timedelta
from django.db.models import Q

pk_url_kwarg = 'post_pk'
# Create your views here.
def showHomePage(request):
    time_thresholdAfter = datetime.now() + timedelta(days=14)
    time_thresholdBefore = datetime.now() - timedelta(days=14)
    festivals = Festival.objects.filter(Q(date__lt=time_thresholdAfter) | Q(date__lt=time_thresholdBefore) )
    
    return render(request,'index.html',{'festivals':festivals})

def festival_each_post_gallery(request,pk):
    festival=Festival.objects.get(pk=pk)
    posts=Post.objects.filter(festival_id=pk).order_by('date')
    content ={
        'posts': posts,
        'festival':festival,
    }
    return render(request,'festival_each.html',content)
    
def post_detail(request,pk):
    # pk_url_kwarg = 'post_id'
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

