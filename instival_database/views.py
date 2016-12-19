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
    return render(request, 'fullFestivalPic.html',{'post':post})
    
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
            return redirect('post_detail.html', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'form': form})
    
#login
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
def getuserid(request):
    if request.method == 'GET':
        name = request.GET['name']
        email = request.GET['email']
        userId = request.GET['userId']
        
        if User.objects.filter(user_id = userId).exists():
            print name + " is using"
            user = User.objects.filter(user_id = userId)[0]
            user.save()
        else:
            User.objects.create (
                name = name,
                email = email
            )
            
    return HttpResponseRedirect(userId)

# def getuser(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#          if form.is_valid():
#             n=form.data.get("name")
#             e=form.data.get("email")
#             p=form.data.get("password")
#             p2=form.data.get("password2")
#             if p==p2:
#                 User.objects.create(name=n,email=e,password=p)
    
#     return render(request, 'login.html')
            