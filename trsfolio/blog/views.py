from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.filter(public=True).order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})



def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'blog/post.html', {'post': post})