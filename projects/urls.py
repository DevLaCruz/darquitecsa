from django.urls import path
from . import views

urlpatterns=[
    path('', views.project, name='projects'),
    path('category/<int:category_id>/', views.category_proj, name='category'),
    path('project/<int:project_id>/', views.project_single_view, name='projects_single')
]