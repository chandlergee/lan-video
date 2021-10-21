from django.contrib import admin
from .models import TVSeries,Episode,Movie,VideoParser,MovieSeries

@admin.register(TVSeries)
class TVSeriesAdmin(admin.ModelAdmin):
    list_display = ('tv_name','tv_country','tv_mtype','description')
    search_fields = ('tv_name',)
    list_per_page = 20

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('e_title','e_url')
    search_fields = ('e_title',)
    list_per_page = 20

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('mv_name','mv_country','mv_mtype','mv_url','description')
    search_fields = ('mv_name',)
    list_per_page = 20

@admin.register(VideoParser)
class VideoParserAdmin(admin.ModelAdmin):
    list_display = ('name','p_url')
    search_fields = ('name',)

@admin.register(MovieSeries)
class MovieSeriesAdmin(admin.ModelAdmin):
    list_display = ('name','电影集','create_date')

    def 电影集(self,series):
        return [x.mv_name for x in series.movies.all()]


admin.site.site_header = '视频后台管理系统'
admin.site.site_title = '视频管理后台'