from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'is_public', 'date_created', 'date_updated']
    list_filter = ['is_public', 'category', 'date_created', 'author']
    search_fields = ['title', 'content', 'author', 'category']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['date_created', 'date_updated']
    list_editable = ['is_public']
    ordering = ['-date_created']
    
    fieldsets = (
        ('Post Content', {
            'fields': ('title', 'slug', 'author', 'category', 'content')
        }),
        ('Settings', {
            'fields': ('is_public',)
        }),
        ('Timestamps', {
            'fields': ('date_created', 'date_updated'),
            'classes': ('collapse',)
        }),
    )
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }