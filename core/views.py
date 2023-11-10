from django.shortcuts import render
from services.models import Services
from blog.models import Post, Category
from projects.models import Project, CategoryProj


# Create your views here.

def home(request):
    services_data = Services.objects.all()  # Obtén todos los datos de servicios
    categories = Category.objects.all()  # Obtén todas las categorías
    recent_posts = Post.objects.order_by('-published')[:4]  # Obtén las 3 publicaciones más recientes
    projects_data = Project.objects.all()
    return render(request, 'core/home.html', {'services': services_data, 'recent_posts': recent_posts, 'categories': categories, 'projects': projects_data})

def about(request):
    return render(request, 'core/about.html')

def sample(request):
    return render(request, 'core/sample.html')

