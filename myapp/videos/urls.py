from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('series/<int:id>',views.episodes),
    path('parser/<int:parser_id>',views.refresh),
    path('movie_series/<int:series_id>',views.movie_series)
]
