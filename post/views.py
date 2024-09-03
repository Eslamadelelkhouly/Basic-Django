from django.shortcuts import render
from .models import Post
# Create your views here.

def post_list(request):
    all_posts = Post.objects.all()   # get data from model
    print(all_posts)
    return render(request , 'all_posts.html' ,{'all_posts': all_posts})


def post_details(request , id):
    post = Post.objects.get(id = id)
    return render(request , 'post.html', {'post':post})