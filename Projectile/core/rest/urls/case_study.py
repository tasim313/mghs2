from django.urls import path
from core.rest.views import case_study

urlpatterns = [
    path('', case_study.CaseStudyCreate.as_view(), name='case-studies-list-create'),
    path('<uuid:uid>/', case_study.CaseStudiesRetrieveUpdate.as_view(),
         name='case-studies-update'),
    path('list/', case_study.CaseStudiesList.as_view(), name='news-events-list'),
]