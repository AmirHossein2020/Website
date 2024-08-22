from django.shortcuts import render
from blog.models import Post


# Create your views here.
def blogView(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html',context)

def SingleView(request):
    return render(request, 'blog/blog-single.html')

