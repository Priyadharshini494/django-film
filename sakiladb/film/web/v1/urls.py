from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views as film_web_v1_views
from .views import FeaturedFilmListView

urlpatterns = [
    path(r"film/", film_web_v1_views.FilmListView.as_view(), name="FWV1FilmListView"),
    #      path(r'film/create/',
    #           film_web_v1_views.ActorCreateView.as_view(), name='FWV1FilmCreateView'),
    #     path(r'film/<int:actor_id>/',
    #          film_web_v1_views.ActorDetailView.as_view(), name='FWV1FilmDetailView'),
    #     path(r'film/<int:pk>/update/',
    #           film_web_v1_views.ActorUpdateView.as_view(), name='FWV1FilmUpdateView'),
    #     # path(r'actor/<int:pk>/delete/',
    #     #      actor_web_v1_views.ActorDeleteView.as_view(), name='AWV1ActorDeleteView'),
    path(r"FeaturedFilmListView/", 
         FeaturedFilmListView.as_view(), name="FeaturedFilmListView"),
]


urlpatterns = format_suffix_patterns(urlpatterns)
