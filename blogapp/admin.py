from django.contrib import admin
from .models import Blog, Comment, HashTag, Youtube
# Register your models here.

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(HashTag)
admin.site.register(Youtube)