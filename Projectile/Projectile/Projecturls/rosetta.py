from django.urls import path, include

urlpatterns = [
    path('rosetta/', include('rosetta.urls')),
]