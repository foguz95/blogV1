from django.contrib import admin
from .models import Article,Comment

admin.site.register(Comment)
#admin.site.register(Article)
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    #diplayde title,author ve oluşturulma bilgsini kolonlarında gösterir
    list_display = ("title","author","created_date")

    #link vermels
    list_display_links = ("title","created_date")
    #title bilgisine göre arama
    search_fields = ("title",)

    # created_date e göre filterladığımız için Tarih süzgeci oluşturur ve filtrelemeyi sağlar.
    list_filter = ("created_date",)
    class Meta:
        model=Article


