from django.urls import path
from core.rest.views import slider_contents

urlpatterns = [
    path('',
         slider_contents.HomeSliderContentCreate.as_view(),
         name='slider-content-list-create'),
    path('<uuid:uid>/',
         slider_contents.HomeSliderContentRetrieveUpdate.as_view(),
         name='slider-content-update'),
    path('list/',
         slider_contents.HomeSliderContentList.as_view(),
         name='slider-content-list'),
    path("file/<uuid:home_content__uid>/", 
         slider_contents.HomeSliderContentFileCreate.as_view(),
         name='slider_content_file_create'),
    path("file/<uuid:uid>/", 
         slider_contents.HomeSliderContentFileRetrieveUpdate.as_view(),
         name='news-events-file-update'),
]