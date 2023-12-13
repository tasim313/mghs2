from django.urls import path
from core.rest.views import appointment

urlpatterns = [
    path('', appointment.AppointmentList.as_view(), name='appointment-list'),
    path('<uuid:uid>/', appointment.AppointmentRetrieveUpdate.as_view(),
         name='appointment-update'),
    path('create/', appointment.AppointmentCreate.as_view(), name='appointment-create'),
]