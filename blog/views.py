from .models import Publication  # new
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
# Create your views here.
class PublicationListView(ListView):
    model = Publication
    template_name = 'publications-list.html'

class PublicationDetailView(DetailView): # new
    model = Publication
    template_name = 'publication-detail.html'

class PublicationCreateView(CreateView):
    model = Publication 
    template_name = 'publication-create.html'
    fields = ['title', 'body', 'author']