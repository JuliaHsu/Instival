from django.shortcuts import render,get_object_or_404,redirect,render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from .models import Post,User,Festival,Country,Festival_Country

from .forms import PostForm
from .forms import CommentForm
from datetime import datetime, timedelta
from django.db.models import Q

from .forms import PostForm,UserForm
from .forms import CommentForm
from django.utils import timezone



# Create your views here.
def showHomePage(request):
    time_thresholdAfter = datetime.now() + timedelta(days=20)
    time_thresholdBefore = datetime.now() - timedelta(days=20)
    festivals = Festival.objects.filter(Q(date__lt=time_thresholdAfter) | Q(date__lt=time_thresholdBefore) )
    countries = Country.objects.all()
    today = datetime.now()
     
    festivals_on_map = Festival_Country.objects.filter(festival__date__month=today.month)
    context={
        'festivals':festivals,
        'countries':countries,
        'festivals_on_map': festivals_on_map,
    }
    return render(request,'index.html',context)


    
    
def showLogin(request):
    return render(request,'login.html',{})
    
def showPersonal(request):
    return render(request,'personal.html',{})
    
def showCalendar(request):
    return render(request,'calendar.html',{})
    

def festival_each_post_gallery(request,pk):
    festival=Festival.objects.get(pk=pk)
    posts=Post.objects.filter(festival_id__festival=pk).order_by('-date')
    content ={
        'posts': posts,
        'festival':festival,
    }
    return render(request,'festival_each_album.html',content)
    

    
def post_detail(request,pk):
    # pk_url_kwarg = 'post_id'
    post = get_object_or_404(Post,pk=pk)
    post_id = post.pk
    liked=False
    if request.session.get('has_liked_'+str(post_id), liked):
        liked = True
        print("liked {}_{}".format(liked, post_id))
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
            'liked':liked,
        }
    return render(request, 'fullFestivalPic.html', context)
   


def like_count_blog(request):
    liked = False
   
    if request.method == 'GET':
        post_id = request.GET['post_id']
        post = Post.objects.get(id=int(post_id))
        if request.session.get('has_liked_'+post_id, liked):
            # request.session['has_liked_'+post_id] = False
            print("unlike")
            if post.like_number > 0:
                likes = post.like_number - 1
                try:
                    del request.session['has_liked_'+post_id]
                except KeyError:
                    print("keyerror")
        else:
            print("like")
            request.session['has_liked_'+post_id] = True
            likes = post.like_number + 1
           
    post.like_number = likes
    post.save()
    return HttpResponse(likes, liked)

def post_document(request):
    u=User.objects.get(name ='Julia2')
    festivals=Festival.objects.order_by('id')
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
    return render(request, 'upload.html', {'festivals':festivals})


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
    festival=Festival_Country.objects.get(pk=pk)
    
    posts=Post.objects.filter(Q(festival_id=pk))
    
    content ={
        'posts': posts,
        'festival':festival,
    }
    return render(request,'festival_each.html',content)




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


            


