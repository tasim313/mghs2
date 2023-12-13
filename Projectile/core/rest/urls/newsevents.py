from django.urls import path
from core.rest.views import newsevents

urlpatterns = [
    path('', newsevents.NewsEventsCreate.as_view(), name='news-events-list-create'),
    path('<uuid:uid>/', newsevents.NewsEventsRetrieveUpdate.as_view(),
         name='news-events-update'),
    path('list/', newsevents.NewsEventsList.as_view(), name='news-events-list'),
    path("file/", 
         newsevents.NewsEventsFileCreate.as_view(),
         name='news_events_file_create'),
    path("file/<uuid:uid>/", 
         newsevents.FileRetrieveUpdate.as_view(),
         name='news-events-file-update'),
]