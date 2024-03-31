from django.shortcuts import render

# Create your views here.
def blogView(request):
    return render(request, 'blog/blog-home.html')

def SingleView(request):
    return render(request, 'blog/blog-single.html')