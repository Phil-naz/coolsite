from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

from django.conf.urls.static import static
from django.contrib import admin

from coolsite import settings
from women.views import *
from django.urls import path, include


from django.views.static import serve as mediaserve
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('women/', include('women.urls')),
    path('women/api/v1/womenlist/', WomenAPIView.as_view()),
    path('captcha/', include('captcha.urls')),
    # path('', include('phil.urls')),
    path('blog/', include('theblog.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', include('phil.urls')),
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
         path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# else:
#     urlpatterns += [
#         url(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$', mediaserve, {'document_root': settings.MEDIA_ROOT}),
#         url(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$', mediaserve, {'document_root': settings.STATIC_ROOT}),
#     ]

handler404 = pageNotFound
