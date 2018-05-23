from django.conf.urls import url, include
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^posts$', views.PostView.as_view(), name='post'),
    url(r'^persons$', views.PersonView.as_view(), name='person'),
	url(r'^uri$', views.UriListView.as_view(), name='uri'),
	url(r'^uri/detail$', views.UriDetailView.as_view(), name='uri_detail'),
	url(r'^test$', views.TestView.as_view())
]



