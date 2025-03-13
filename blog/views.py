from django.views.generic import ListView, DetailView  # new
from .models import Publication

# Create your views here.
class PublicationListView(ListView):
    model = Publication
    template_name = 'publications-list.html'

class PublicationDetailView(DetailView): # new
    model = Publication
    template_name = 'publication-detail.html'