from django.contrib import admin

from .models import Photo, Writing, Tag, Photo_Comment, Writing_Comment

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'published_date')
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    def publish(self, request, queryset):
        queryset.update(published=True)

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on', 'post')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)




admin.site.register(Photo, PhotoAdmin)
admin.site.register(Writing)
admin.site.register(Tag)
admin.site.register(Photo_Comment, CommentAdmin)
admin.site.register(Writing_Comment, CommentAdmin)