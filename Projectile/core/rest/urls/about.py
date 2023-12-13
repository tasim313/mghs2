from django.urls import path
from core.rest.views import about

urlpatterns = [
    path('', 
         about.AboutCreate.as_view(),
         name='about-list-create'),
    path('<uuid:uid>/',
         about.AboutRetrieveUpdate.as_view(),
         name='about-update'),
    path('list/', 
         about.AboutList.as_view(),
         name='about-list'),
    
    path('file/<uuid:uid>/', about.AboutFileRetrieveUpdate.as_view(),
         name='about-file-update'),
    path('file/list/', 
         about.AboutFileList.as_view(),
         name='about-file-list'),
]