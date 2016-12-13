from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post


# from .forms import AddPost
# Create your views here.

def festival_each_post_gallery(request):
    posts=Post.objects.order_by('date')
    return render(request,'festival_each.html', {'posts':posts})
def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'fullFestivalPic.html',{'post':post})
    
#def upload(request):
#    if request.method == 'GET':
#        return render(request,"instival_app/Template/upload.html")
#    if request.method == 'POST':
#        django_form = AddPost(request.POST)
#        if django_form.is_valid():
#            new_post_text = django_form.data.get("text")
#            Post.objects.create(text = new_post_text,)
#            return HttpResponseRedirect("/") 