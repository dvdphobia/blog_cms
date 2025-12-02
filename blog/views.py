from django.shortcuts import render
from blog.models import Post, Comment


# Create your views here.

def blog_index(request):
    posts = Post.object.all().order_by('-created_at')
    context = {
        "posts": posts
    }

    return render(request, "blog/index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(category__name=category)   # ← category (singular) NOT categories
    context = {
        'category_name': category,
        'posts': posts
    }
    return render(request, 'blog/categories.html', context)


def blog_detail(request, pk):

    post = Post.objects.get(pk=pk)

    comments = Comment.objects.filter(post=post)

    context = {

        "post": post,

        "comments": comments,

    }


    return render(request, "blog/detail.html", context)



    