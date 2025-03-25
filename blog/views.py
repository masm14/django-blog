from .models import Publication  # new
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
                                        LoginRequiredMixin, 
                                        UserPassesTestMixin,
                                        )
# Create your views here.
class PublicationListView(ListView):
    model = Publication
    template_name = 'publications-list.html'

class PublicationDetailView(LoginRequiredMixin, DetailView): # new
    model = Publication
    template_name = 'publication-detail.html'

class PublicationCreateView(LoginRequiredMixin, CreateView):
    model = Publication 
    template_name = 'publication-create.html'
    fields = ['title', 'body', 'author']

class PublicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # new
    model = Publication
    template_name = 'publication-update.html'
    fields = ['title', 'body',]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PublicationDeleteView(LoginRequiredMixin, DeleteView):
    model = Publication
    template_name = 'publication-delete.html'
    success_url = reverse_lazy('publications-list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user