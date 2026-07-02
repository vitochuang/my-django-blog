from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-created_at') # 撈取所有文章
    return render(request, 'blog/index.html', {'posts': posts})
