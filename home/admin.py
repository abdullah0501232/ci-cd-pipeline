from django.contrib import admin
from .models import Skill, Project, BlogPost, ContactMessage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_featured',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Skill)
admin.site.register(ContactMessage)