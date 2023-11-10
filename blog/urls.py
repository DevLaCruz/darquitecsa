from django.urls import path
from . import views

urlpatterns=[
    path('', views.blog, name='blog'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('post/<int:post_id>/', views.blog_single_view, name='blog_single'),
]