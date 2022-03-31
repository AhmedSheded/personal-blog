from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = 'Sheded Blog'
admin.site.site_title = 'Sheded Blog'

admin.site.register(Post)
admin.site.register(Comment)