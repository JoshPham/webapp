from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.all()
    context = {
        'title': "Home",
        'posts': posts,
    }
    return render(request, 'mainapp/home.html', context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'title': post.title,
        'post': post,
    }
    return render(request, 'mainapp/post.html', context)

def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {
        'title': "Create Post",
        'form': form
    }
    return render(request, 'mainapp/post_form.html', context)