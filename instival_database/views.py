from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import Post,User,Festival

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
    
    return render(request,'index.html',{'festivals':festivals})
    
def showLogin(request):
    return render(request,'login.html',{})
    
def showPersonal(request):
    return render(request,'personal.html',{})
    
def showCalendar(request):
    return render(request,'calendar.html',{})
    
def festival_each_post_gallery(request,pk):
    festival=Festival.objects.get(pk=pk)
    posts=Post.objects.filter(festival_id=pk).order_by('-date')
    content ={
        'posts': posts,
        'festival':festival,
    }
    return render(request,'festival_each.html',content)
    
def country_album(request):
   
    return render(request,'festival_each.html',{})
    
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



#login
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
def getuserid(request):
    if request.method == 'GET':
        name = request.GET['name']
        email = request.GET['email']
        userId = request.GET['userId']
        print(userId)
        if User.objects.filter(userId = userId).exists():
            print name + " is using"
            user = User.objects.filter(userId = userId)[0]
            user.save()
        else:
            User.objects.create (
                userId = userId,
                name = name,
                email = email
            )
        
    return HttpResponseRedirect(userId)


            

