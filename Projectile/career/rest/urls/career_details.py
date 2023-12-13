from django.urls import path
from career.rest.views import career_details

urlpatterns = [
    path('', 
         career_details.CareerDetailsCreate.as_view(),
         name='career-details-list-create'),
    path('<uuid:uid>/',
         career_details.CareerDetailsRetrieveUpdate.as_view(),
         name='career-details-update'),
    path('<uuid:uid>/list/', 
         career_details.CareerDetailsList.as_view(),
         name='career-details-list'),
]