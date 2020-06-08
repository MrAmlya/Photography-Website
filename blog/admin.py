from django.contrib import admin
from .models import Gallery
from .models import Post
# Register your models here.
admin.site.register(Post)
admin.site.register(Gallery)