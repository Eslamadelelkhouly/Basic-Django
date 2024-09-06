from django.shortcuts import render
# Create your views here.

from .models import Post
from .forms import PostForm

def post_list(request):
    all_posts = Post.objects.all()
    print(all_posts)
    return render(request,'post/post_list.html',{'all_posts':all_posts})

def post_details(request , id):
    post = Post.objects.get(id=id)
    return render(request,'post/post_details.html',{'post':post})


def post_create(request):
    if request.method == "POST":
        print('in post')
        form = PostForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        print('in else')
        form = PostForm()
    return render(request , 'post/post_create.html',{'form':form})


def post_edit(request):
    pass