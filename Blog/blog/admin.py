from django.contrib import admin
from .models import Category, Language, Uri 

admin.site.register(Uri)
admin.site.register(Language)
admin.site.register(Category)


