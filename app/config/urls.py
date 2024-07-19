from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path("", include("kitchen_sink.urls")),
    path("admin/", admin.site.urls),
]


if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
