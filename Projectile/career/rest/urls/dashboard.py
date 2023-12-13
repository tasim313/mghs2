from django.urls import path
from career.rest.views import dashboard

urlpatterns = [
    path('', 
         dashboard.DashboardAPIViewList.as_view(),
         name='dashboard'),
    
]