from snippets import views

__author__ = 'frank'
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('snippets.views',
                       url(r'snippets/$', views.SnippetList.as_view()),
                       url(r'snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
