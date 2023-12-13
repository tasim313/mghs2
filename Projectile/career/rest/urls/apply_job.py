from django.urls import path
from career.rest.views import apply_job

urlpatterns = [
    path('', 
         apply_job.ApplyJobCreate.as_view(),
         name='job-candidate-create'),
    path('list/',
         apply_job.ApplyJobList.as_view(),
         name='candidate-list'),
    path('<uuid:uid>/list/', 
         apply_job.ApplyJobListForSpecificJobCategory.as_view(),
         name='job-candidate-list'),
]