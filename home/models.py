from django.db import models
from django.utils import timezone

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    proficiency = models.PositiveIntegerField(default=80)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300, help_text="Comma-separated, e.g. Python, Django")
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d')}"