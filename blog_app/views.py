from django.shortcuts import render, get_object_or_404
from .models import Blogs


# Create your views here.
def blog_list(request):
    blogs = Blogs.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'blogs': blogs})


def blog_detail(request, pk):
    blog = get_object_or_404(Blogs, pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})
