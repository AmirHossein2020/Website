from django.contrib import admin
from blog.models import Post
# Register your models here.

#@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty'
    list_display = ('title','author','conted_views','created_date','status',)
    list_filter = ('status',)
    search_fields = ('title', 'content',)
    
admin.site.register(Post, PostAdmin)