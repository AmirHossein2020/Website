from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    images = models.ImageField(upload_to='blog/', default='blog/static/img/about-img.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    #tag
    # category
    conted_views = models.IntegerField(default=0)
    status = models.BooleanField()
    published_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return " {} {} ".format(self.title,self.id)