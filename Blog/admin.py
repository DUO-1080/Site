from django.contrib import admin
from .models import Artical,Tag,Comment
# Register your models here.
admin.site.register(Artical)
admin.site.register(Tag)
admin.site.register(Comment)