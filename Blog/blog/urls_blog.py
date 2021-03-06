from django.conf.urls import url, include
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
	url(r'^uri$', views.UriListView.as_view(), name='uri'),
	url(r'^uri/(?P<pk>\d+)/$', views.UriDetailView.as_view(), name='uri_detail'),
]


