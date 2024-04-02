from django.contrib import admin
from .models import Resume , Project , Language , Professional_skill
# Register your models here.

admin.site.register(Resume)
admin.site.register(Project)
admin.site.register(Language)
admin.site.register(Professional_skill)