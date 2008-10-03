from django.contrib import admin
from models import Category, Post

class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {
        'slug': ('title',)
    }

class PostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'publish', 'status')
    list_filter   = ('publish', 'categories', 'status')
    search_fields = ('title', 'body')

    prepopulated_fields = {'slug': ('title',)}
    radio_fields = {'status': admin.VERTICAL}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

