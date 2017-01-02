from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import Post,User,Festival,Country,Festival_Country,Profile

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
     
    festivals_on_map = Festival_Country.objects.filter(festival__date__month=today.month)
    context={
        'festivals':festivals,
        'countries':countries,
        'festivals_on_map': festivals_on_map,
    }
    return render(request,'index.html',context)

def showLogin(request):
    return render(request,'login.html',{})
    
def showPersonal(request,user):
    
    # profiledataas=Users.objects.filter()
    
    # content ={
    #     'profiledata': profiledatas,
    # }
    
    users=User.objects.get(id=user)
    profiles=Profile.objects.get(user_id__id=user)
    posts=Post.objects.filter(user_id__id=user).order_by('-date')
    content ={
        'posts': posts,
        'profiles': profiles,
        'users':users,
    }
    
    return render(request,'personal.html',content)
    
    ############################
    
def setProfile_view(request,user):
    
    # profiledataas=Users.objects.filter()
    
    # content ={
    #     'profiledata': profiledatas,
    # }
    
    users=User.objects.get(id=user)
    profiles=Profile.objects.get(user_id__id=user)
    posts=Post.objects.filter(user_id__id=user).order_by('-date')
    content ={
        'posts': posts,
        'profiles': profiles,
        'users':users,
    }
    
    if request.method == "POST":
        if 'intro' in request.POST:
            Profile.objects.filter(user_id=user).update(self_introduction=request.POST['intro'])
    
    return render(request,'setProfile.html',content)
    
    ######################
    
def upload_personalPhoto(request,user):
    users=User.objects.get(id=user)
    content ={
        'users':users,
    }
    
    if request.method == "POST":
        if 'picture' in request.POST:
            Profile.objects.filter(user_id=user).update(profile_picture=request.POST['picture'])
    return render(request,'upload_photo.html',content)
    
def showCalendar(request):
    return render(request,'calendar.html',{})
    

def festival_each_post_gallery(request,pk):
    festival=Festival.objects.get(pk=pk)
    posts=Post.objects.filter(festival_id__festival=pk).order_by('-date')
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
    


            

def post_document(request,user):
    u=User.objects.get(id=user)
    festivals=Festival_Country.objects.order_by('id')
    Countrys=Country.objects.order_by('id')
    
    context = {
        'users' : u,
        'festivals' : festivals,
        'Countrys' : Countrys,
    }
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = u
            f=form.data.get("getfestival")
            f_f=Festival.objects.get(name =f.split('.')[0])
            f_c=Country.objects.get(name =f.split('.')[1])
            paa=Festival_Country.objects.get(festival=f_f,location=f_c)
            post.festival_id = paa
            p=form.data.get("picture")
            c=form.data.get("getlocation")
            post.location=Country.objects.get(name = c)
            post.picture = p
            post.date = timezone.now()
            post.like_id_group = ""
            post.comment_id_group = ""
            post.like_number = 0
            post.save()
    return render(request, 'upload.html', context)


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

   ############################################
   
def country_each_festival_album(request,name,pk):
    festival=Festival_Country.objects.get(pk=pk)
    
    posts=Post.objects.filter(Q(festival_id=pk))
    
    content ={
        'posts': posts,
        'festival':festival,
    }
    return render(request,'festival_each.html',content)

    ##############################################


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
    
    


            


