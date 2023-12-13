from django.urls import include, path

urlpatterns = [ 
    path("job/", include("career.rest.urls.career")),
    path("job/details/", include("career.rest.urls.career_details")),
    path("studies/details/", include("career.rest.urls.case_study_details")),
    path('news_events/details/', include("career.rest.urls.news_event_details")),
    path('candidate/', include("career.rest.urls.apply_job")),
    path('video/', include("career.rest.urls.intro_video")),
    path('message/', include("career.rest.urls.message")),
    path('dashboard/', include("career.rest.urls.dashboard")),
]