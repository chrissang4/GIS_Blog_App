from django.contrib import admin
from .models import Post, Author

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    list_filter = ('date_posted', 'author')
    search_fields = ('title', 'description')
    date_hierarchy = 'date_posted'
    ordering = ('-date_posted',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_joined')
    
    def rename(self, request, queryset):
        queryset.update(name="Author")
        
    rename.short_description = "Rename selected authors"
    
    actions = ['rename']

    
    

admin.site.site_header = 'GIS App'
admin.site.site_title = 'GIS/RS Blog'
admin.site.index_title = 'THE SCIENCE OF WHERE'




# from django.contrib import admin
# from .models import Post
# # Register your models here.
# admin.site.register(Post)
