from blog.models import Post , Category
from django.template import Library

register = Library()

@register.inclusion_tag('blog/blog-post-cat.html')
def post_category():
    posts = Post.objects.filter(status=1)
    categorys = Category.objects.all()
    cat_dict = {}
    for name in categorys:
        cat_dict[name] = posts.filter(category=name).count()

    return {'categorys': cat_dict}

@register.inclusion_tag('blog/blog-post-p.html')
def latest_post():
    posts = Post.objects.filter(status=1).order_by('published_date')[:2]
    return {'posts': posts}