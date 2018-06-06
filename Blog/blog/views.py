from django.shortcuts import render_to_response
from django.views import generic
from blog.models import Uri
from django.shortcuts import render, get_object_or_404
from django.conf.urls import url
from django.utils import timezone

# Create your views here.
class UriListView(generic.ListView):
    model = Uri

    def get_queryset(self):   
    	a = Uri.objects.all() 	
    	b = Uri.objects.filter(language_type__programming_language = "C")
    	c = Uri.objects.filter(title__icontains = 'Extremamente') 
    	d = Uri.objects.filter(pub_date__lte = timezone.now(),title__icontains = '2')
    	e = Uri.objects.filter(pub_date = timezone.now())	
    	f = Uri.objects.filter(title = 'URI 1001 - Extremamente Basico')
    	return b

class UriDetailView(generic.DetailView):				# problema no Uri.objects.get(id=?) ??
    model = Uri                                              # __lte
                                                             # __icontains
class IndexView(generic.ListView):                       # __startswith
    model = Uri
    template_name = 'blog/index.html'                        # __contains
    
    def get_queryset(self):   
        e = Uri.objects.filter(pub_date = timezone.now())   
        return e   