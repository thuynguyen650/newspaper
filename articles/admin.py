from django.contrib import admin
from .models import Article, Comment
from django.contrib import admin
# Register your models here.
class CommentInLine(admin.TabularInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInLine,]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)