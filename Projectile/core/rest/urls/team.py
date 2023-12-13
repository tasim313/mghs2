from django.urls import path
from core.rest.views import team

urlpatterns = [
    path('list/',
         team.TeamAPIView.as_view(),
         name='team-list-create'),
    path('<uuid:uid>/', team.TeamRetrieveUpdate.as_view(),
         name='teams-update'),
    path('', team.TeamCreateAPIView.as_view(), name='teams-list'),
]