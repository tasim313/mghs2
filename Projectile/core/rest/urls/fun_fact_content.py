from django.urls import path
from core.rest.views import fun_fact_content

urlpatterns = [
    path('<uuid:uid>/',
         fun_fact_content.FunFactContentRetrieveUpdate.as_view(),
         name='about-update'),
    path('list/', 
         fun_fact_content.FunFactContentList.as_view(),
         name='fun-fact-list'),
]