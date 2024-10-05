from .views import blog_list, blog_detail
from django.urls import path

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('blog/<int:pk>/', blog_detail, name='blog_detail'),
]
