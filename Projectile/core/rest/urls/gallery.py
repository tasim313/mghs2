from django.urls import path
from core.rest.views import gallery

urlpatterns = [
    path('',
         gallery.GalleryCreate.as_view(),
         name='gallery-list-create'),
    path('<uuid:uid>/', gallery.GalleryRetrieveUpdate.as_view(),
         name='gallery-update'),
    path('list/', gallery.GalleryList.as_view(), name='gallery-list'),
]