from django.shortcuts import render, get_object_or_404
from apps.api.models import Post


def blog_list(request):
    """Display all public blog posts"""
    posts = Post.objects.filter(is_public=True).order_by('-date_created')
    context = {'posts': posts}
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):
    """Display a single blog post by slug"""
    post = get_object_or_404(Post, slug=slug, is_public=True)
    context = {'post': post}
    return render(request, 'blog/blog_detail.html', context)

