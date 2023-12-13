from django.urls import path
from career.rest.views import news_event_details

urlpatterns = [
    
    path('update/<uuid:uid>/',
         news_event_details.NewsEventsDetailsRetrieveUpdate.as_view(),
         name='news-events-details-update'),
    path('<uuid:uid>/list/', 
         news_event_details.NewsEventsDetailsList.as_view(),
         name='news-events-details-list'),
    path('', 
         news_event_details.NewsEventsDetailsCreate.as_view(),
         name='news-events-details-create'),
]