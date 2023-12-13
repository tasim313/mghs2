from django.urls import path, include

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('webns/auth/', include('djoser.urls.authtoken')),
    path('jwt/', include('djoser.urls.jwt')),
]