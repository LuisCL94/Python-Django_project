from django.shortcuts import render_to_response
from django.views import generic
from .models import Post, Person

# Create your views here.
class PostView(generic.ListView):
    template_name = 'blog/test.html'
    model = Post
    context_object_name = 'posts'


class PersonView(generic.ListView):
    template_name = 'blog/models_test.html'
    model = Person
    context_object_name = 'persons'    



