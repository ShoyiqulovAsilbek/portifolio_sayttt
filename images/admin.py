from django.contrib import admin
from .models import  Contact, Article,Comment


admin.site.register(( Contact))

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=["title","create_data","is_active"]
    list_filter = ["is_active"]

admin.site.register(Comment)