from django.shortcuts import render_to_response
from django.views import generic
from .models import Post, Person, Uri
from django.shortcuts import render, get_object_or_404
from django.conf.urls import url

# Create your views here.
class PostView(generic.ListView):
    model = Post
    #template_name = 'blog/post_list.html'
    #context_object_name = 'object_list' ou 'post_list'

class PersonView(generic.ListView):
    template_name = 'blog/person_list.html'
    model = Person
    context_object_name = 'persons'    

class UriListView(generic.ListView):
    model = Uri
   
class UriDetailView(generic.DetailView):
    model = Uri
    
class IndexView(generic.TemplateView):
    template_name = 'blog/test.html'
        
