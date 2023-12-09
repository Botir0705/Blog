from django.urls import path
from .views import blog_index, blog_category, blog_detail, blog_create


urlpatterns = [
    path('', blog_index, name='blog_index'),
    path('category/<str:category>', blog_category, name='blog_category'),
    path('detail/<int:pk>', blog_detail, name='blog_detail'),
    path('create/', blog_create, name='blog_create')
]
