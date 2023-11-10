from django.shortcuts import render, get_object_or_404
from . models import Project, CategoryProj

# Create your views here.

def project(request):
    projects= Project.objects.all()
    categories = CategoryProj.objects.all()  # Obtener todas las categorías
    selected_category = request.GET.get('category')  # Obtener el parámetro 'category' de la solicitud GET

    if selected_category and selected_category != 'All':
        projects = projects.filter(categories__id=selected_category)

    return render(request, 'projects/projects.html', {'projects': projects, 'categories': categories})
  

def category_proj(request, category_id):
    category=get_object_or_404(CategoryProj,id=category_id)
    return render(request, 'projects/category_proj.html', {'categories':category})

#En singular
def project_single_view(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, 'projects/projects_single.html', {'project': project})
