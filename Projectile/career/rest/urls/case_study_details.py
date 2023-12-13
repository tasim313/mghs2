from django.urls import path
from career.rest.views import case_study_details

urlpatterns = [
    
    path('update/<uuid:uid>/',
         case_study_details.CaseStudyDetailsRetrieveUpdate.as_view(),
         name='case-study-details-update'),
    path('<uuid:uid>/list/', 
         case_study_details.CaseStudyDetailsList.as_view(),
         name='case-study-details-list'),
    path('<uuid:case_study__uid>/create/', 
         case_study_details.CaseStudyDetailsCreate.as_view(),
         name='case-study-details-create'),
]