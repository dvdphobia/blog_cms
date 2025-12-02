from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_public', 'date_created', 'date_updated']
    list_filter = ['is_public', 'date_created', 'author']
    search_fields = ['title', 'content', 'author']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['date_created', 'date_updated']
    list_editable = ['is_public']
    ordering = ['-date_created']
    
    fieldsets = (
        ('Post Content', {
            'fields': ('title', 'slug', 'author', 'content')
        }),
        ('Settings', {
            'fields': ('is_public',)
        }),
        ('Timestamps', {
            'fields': ('date_created', 'date_updated'),
            'classes': ('collapse',)
        }),
    )