from django.contrib import admin
from .models import Article, Comment

class CommentInline(admin.StackedInline):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    # list_display = ('title', 'author', 'created_at')
    # list_filter = ('created_at',)
    # search_fields = ('title',)
    # date_hierarchy = 'created_at'
    # ordering = ('-created_at',)
    # filter_horizontal = ('tags',)
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    # autocomplete_lookup_fields = {'fk': ['author']}
    # readonly_fields = ('created_at',)
    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'slug', 'author', 'tags', 'content', 'created_at')
    #     }),
    # )
    # actions = ['make_published']

    # def make_published(self, request, queryset):
    #     queryset.update(status='p')
    #     self.message_user(request, 'Articles marked as published')
    # make_published.short_description = 'Mark selected articles as published'
    # make_published.allowed_permissions = ('change',)


admin.site.register(Article, ArticleAdmin)

admin.site.register(Comment)


