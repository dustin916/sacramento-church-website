from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('website.urls')),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catalog'),
    path('managers/', include('django.contrib.auth.urls')),
    path('managers/', include('managers.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configure Admin Titles
admin.site.site_header = "Sacramento WMC Admin Page"
admin.site.site_title = "Sacramento WMC Admin Page"
admin.site.index_title = ""
