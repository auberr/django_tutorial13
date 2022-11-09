from django.contrib import admin
from articles.models import Article
from articles.models import Category
from articles.models import Comment

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)