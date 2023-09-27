from django.contrib import admin
from .models import Post, signup, Category, Profile, Comment

# Register your models here.

admin.site.register(Post)
admin.site.register(signup)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)


