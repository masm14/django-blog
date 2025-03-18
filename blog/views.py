from .models import Publication  # new
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

class PublicationUpdateView(UpdateView): # new
    model = Publication
    template_name = 'publication-update.html'
    fields = ['title', 'body',]

class PublicationDeleteView(DeleteView):
    model = Publication
    template_name = 'publication-delete.html'
    success_url = reverse_lazy('publications-list')