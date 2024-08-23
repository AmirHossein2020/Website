from django.shortcuts import render , get_object_or_404
from blog.models import Post


# Create your views here.
def blogView(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html',context)

def SingleView(request,pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)

