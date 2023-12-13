from django.urls import path
from career.rest.views import career

urlpatterns = [
    path('', 
         career.CareerCreate.as_view(),
         name='career-list-create'),
    path('<uuid:uid>/',
         career.CareerRetrieveUpdate.as_view(),
         name='career-update'),
    path('list/', 
         career.CareerList.as_view(),
         name='career-list')
]