from django.urls import path, include

urlpatterns = [
     path("career/", include("career.rest.urls")),
]