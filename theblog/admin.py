from django.contrib import admin
from theblog.models import Post, Comment, Notification


admin.site.site_header="amira"
admin.site.site_title="mera"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'total_likes')
    search_fields = ('title', 'body')
    list_filter = ('author', 'date')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'body', 'date')
    search_fields = ('body',)
    list_filter = ('date',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'user', 'created_at')


