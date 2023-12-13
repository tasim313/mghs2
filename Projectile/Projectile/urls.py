from django.conf.urls.static import static
from django.conf import settings

from .Projecturls.admin import urlpatterns as admin
from .Projecturls.djoser import urlpatterns as auth
from .Projecturls.debug_toolbar import urlpatterns as debug
from .Projecturls.health import urlpatterns as health
from .Projecturls.swagger import urlpatterns as swagger
from .Projecturls.rosetta import urlpatterns as rosetta
from .Projecturls.core import urlpatterns as core
from .Projecturls.career import urlpatterns as career

urlpatterns = []
urlpatterns.extend(admin)
urlpatterns.extend(auth)
urlpatterns.extend(debug)
urlpatterns.extend(health)
urlpatterns.extend(swagger)
urlpatterns.extend(rosetta)
urlpatterns.extend(core)
urlpatterns.extend(career)

# Add static URLs for serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(
        settings.MEDIA_URL_2,
        document_root=settings.MEDIA_ROOT)

# urlpatterns = (
#     admin+
#     auth+
#     debug+
#     health+
#     swagger+
#     rosetta+
#     core+
#     career
# ) + static(
#     settings.MEDIA_URL,
#     document_root=settings.MEDIA_ROOT
#     ) + static(
#         settings.MEDIA_URL_2,
#         document_root=settings.MEDIA_ROOT)
