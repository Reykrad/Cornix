from django.conf.urls import include, url
from django.contrib import admin
from apps.blog.views import IndexView, ArtDet

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view()),
    url(r'^articulo/(?P<slug>[-\w]+)/$', ArtDet.as_view()),
    #url(r'^articulo/(?P<page>[0-9]+)/$', IndexView.as_view()),
    url(r'^$', IndexView.as_view()),
]
