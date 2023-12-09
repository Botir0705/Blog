from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.http import HttpResponseRedirect


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts
    }
    return render(request, 'blog_app/index.html', context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by('-created_on')
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'blog_app/category.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }
    return render(request, "blog_app/detail.html", context)

def blog_create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'blog_app/create.html', context)
        
        