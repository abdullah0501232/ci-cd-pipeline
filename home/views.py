from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Skill, BlogPost
from .forms import ContactForm

def home(request):
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    return render(request, 'home/home.html', {'projects': featured_projects})

def about(request):
    skills = Skill.objects.all()
    return render(request, 'home/about.html', {'skills': skills})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'home/project_list.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'home/project_detail.html', {'project': project})

def blog_list(request):
    posts = BlogPost.objects.filter(published=True)
    return render(request, 'home/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    return render(request, 'home/blog_detail.html', {'post': post})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'home/contact_success.html')