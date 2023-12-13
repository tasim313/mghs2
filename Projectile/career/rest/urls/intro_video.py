from django.urls import path
from career.rest.views import intro_video

urlpatterns = [
    path('', 
         intro_video.IntroVideoCreate.as_view(),
         name='video-list-create'),
    path('<uuid:uid>/',
         intro_video.IntroVideoRetrieveUpdate.as_view(),
         name='video-update'),
    path('list/', 
         intro_video.IntroVideoList.as_view(),
         name='video-list'),
]