from django.shortcuts import render
from .models import Post
# Create your views here.
def index(requset):
    posts = Post.objects.all()
    return render(requset, 'index.html', {'posts': posts})

def post(reqeust, pk):
    post = Post.objects.get(id=pk)
    return render(reqeust, 'post.html', {'post': post})
