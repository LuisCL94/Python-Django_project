from django.shortcuts import render_to_response
from django.views import generic
from .models import Post, Person, Uri

# Create your views here.
class PostView(generic.ListView):
    template_name = 'blog/post_list.html'
    model = Post
    context_object_name = 'posts'

class PersonView(generic.ListView):
    template_name = 'blog/person_list.html'
    model = Person
    context_object_name = 'persons'    

class UriListView(generic.ListView):
    template_name = 'blog/uri_list.html'
    model = Uri
    context_object_name = 'uri_list'

class UriDetailView(generic.ListView):
    template_name = 'blog/uri_detail.html'
    model = Uri
    context_object_name = 'uri_detail'

class TestView(generic.TemplateView):
    template_name = 'blog/test.html'
        