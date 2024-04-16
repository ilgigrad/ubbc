"""ubbc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.utils.translation import ugettext_lazy as _

i18n_urlpatterns = i18n_patterns(
    # path("controlroom/", admin.site.urls),
    url(r"^user/", include("user.urls", namespace="user")),
    url(r"^athlete/", include("athlete.urls", namespace="athlete")),
    url(r"^volunteer/", include("volunteer.urls", namespace="volunteer")),
    url(r"^event/", include("event.urls", namespace="event")),
    url(r"^race/", include("race.urls", namespace="race")),
)

normal_patterns = [
    path("controlroom/", admin.site.urls),
]

drf_urlpatterns = []

urlpatterns = (
    i18n_urlpatterns + normal_patterns + drf_urlpatterns + staticfiles_urlpatterns()
)
if settings.DEBUG_TOOLBAR:
    import debug_toolbar

    urlpatterns += [
        url(r"^__debug__/", include(debug_toolbar.urls)),
    ]

# dev app
admin.site.site_header = _("UBBC Administration Console")
admin.site.site_title = "UBBC Control Room"
admin.site.index_title = _("Welcome to the UBBC Administration Console")
