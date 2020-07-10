from django.contrib import admin

# Register your models here.
from .models import Article,Comment
admin.site.register(Comment)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('id','title','created_date')
    list_display_links=('title','created_date')
    list_filter=('created_date',)
    search_fields=('title',)
    # show_full_result_count=True
    # save_on_top=True
    # save_as=True
    # list_editable=('title',)
    
    class Meta:
        model=Article
