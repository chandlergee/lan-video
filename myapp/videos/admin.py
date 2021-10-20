from django.contrib import admin
from .models import TVSeries,Episode,Movie,VideoParser,MovieSeries

class TVSeriesAdmin(admin.ModelAdmin):
    list_display = ('tv_name','tv_country','tv_mtype','description')
    search_fields = ('tv_name',)
    list_per_page = 20

class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('e_title','e_url')
    search_fields = ('e_title',)
    list_per_page = 20

class MovieAdmin(admin.ModelAdmin):
    list_display = ('mv_name','mv_country','mv_mtype','mv_url','description')
    search_fields = ('mv_name',)
    list_per_page = 20

class VideoParserAdmin(admin.ModelAdmin):
    list_display = ('name','p_url')
    search_fields = ('name',)

class MovieSeriesAdmin(admin.ModelAdmin):
    list_display = ('name','create_date')
    search_fields = ('name',)

# Register your models here.
admin.site.site_header = '视频后台管理系统'
admin.site.site_title = '视频管理后台'
admin.site.register(TVSeries,TVSeriesAdmin)
admin.site.register(Episode,EpisodeAdmin)
admin.site.register(Movie,MovieAdmin)
admin.site.register(VideoParser,VideoParserAdmin)
admin.site.register(MovieSeries,MovieSeriesAdmin)