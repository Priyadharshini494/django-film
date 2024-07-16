from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views as actor_web_v1_views

urlpatterns = [
    path(r'actor/', 
         actor_web_v1_views.ActorListView.as_view(), name='AWV1ActorListView'),
     path(r'actor/create/', 
          actor_web_v1_views.ActorCreateView.as_view(), name='AWV1ActorCreateView'),
    path(r'actor/<int:actor_id>/', 
         actor_web_v1_views.ActorDetailView.as_view(), name='AWV1ActorDetailView'),
    path(r'actor/<int:pk>/update/', 
          actor_web_v1_views.ActorUpdateView.as_view(), name='AWV1ActorUpdateView'),
    # path(r'actor/<int:pk>/delete/', 
    #      actor_web_v1_views.ActorDeleteView.as_view(), name='AWV1ActorDeleteView'),
]

urlpatterns = format_suffix_patterns(urlpatterns)