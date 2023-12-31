from django.shortcuts import render, get_object_or_404
from . models import Post, Category

# Create your views here.

def blog(request):
    posts= Post.objects.all()
    categories = Category.objects.all()  # Obtener todas las categorías
    selected_category = request.GET.get('category')  # Obtener el parámetro 'category' de la solicitud GET

    if selected_category and selected_category != 'All':
        posts = posts.filter(categories__id=selected_category)

    return render(request,'blog/blog.html', {'posts':posts, 'categories': categories})


def category(request, category_id):
    category=get_object_or_404(Category,id=category_id)
    return render(request, 'blog/category.html', {'category':category})


def blog_single_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blog/blog_single.html', {'post': post})

