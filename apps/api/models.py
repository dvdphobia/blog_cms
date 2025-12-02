from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the blog post title")
    author = models.CharField(max_length=100, help_text="Author name")
    is_public = models.BooleanField(default=True, help_text="Check to publish this post")
    content = models.TextField(help_text="Write your blog content here")
    slug = models.SlugField(unique=True, max_length=200, help_text="URL-friendly version of title (auto-filled)")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title
    