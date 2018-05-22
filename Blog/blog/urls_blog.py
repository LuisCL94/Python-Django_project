from django.conf.urls import url, include
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^post$', views.PostView.as_view(), name='post'),
    url(r'^hall/$', views.PersonView.as_view(), name='models'),
]



