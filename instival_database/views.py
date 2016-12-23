from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import Post,User,Festival,Country

from .forms import PostForm
from .forms import CommentForm
from datetime import datetime, timedelta
from django.db.models import Q

from .forms import PostForm,UserForm
from .forms import CommentForm
from django.utils import timezone


pk_url_kwarg = 'post_pk'
# Create your views here.
def showHomePage(request):
    time_thresholdAfter = datetime.now() + timedelta(days=20)
    time_thresholdBefore = datetime.now() - timedelta(days=14)
    festivals = Festival.objects.filter(Q(date__lt=time_thresholdAfter) | Q(date__lt=time_thresholdBefore) )
    countries = Country.objects.all()
    today = datetime.now()
    
    festivals_on_map = Festival.objects.filter(date__month=today.month)
    context={
        'festivals':festivals,
        'countries':countries,
        'festivals_on_map': festivals_on_map,
    }
    return render(request,'index.html',context)

def festival_each_post_gallery(request,pk):
    festival=Festival.objects.get(pk=pk)
    posts=Post.objects.filter(festival_id=pk).order_by('-date')
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
    
def post_document(request):
    u=User.objects.get(name ='Julia2')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = u
            f=form.data.get("festival")
            post.festival_id = Festival.objects.get(name = f)
            p=form.data.get("picture")
            post.picture=p
            post.date = timezone.now()
            post.like_id_group = ""
            post.comment_id_group = ""
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
    

def createAccount(request):
    
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            n=form.data.get("name")
            e=form.data.get("email")
            p=form.data.get("password")
            p2=form.data.get("password2")
            if p==p2:
                User.objects.create(name=n,email=e,password=p)
    
    return render(request, 'signup.html')
def country_each_festival_album(request,name,pk):
    festival=Festival.objects.get(pk=pk)
    
    posts=Post.objects.filter(Q(festival_id=pk) & Q(location=name))
    
    content ={
        'posts': posts,
        'festival':festival,
    }
    return render(request,'festival_each.html',content)
