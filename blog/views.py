from django.views.generic import ListView
from .models import Publication

# Create your views here.
class PublicationListView(ListView):
    model = Publication
    template_name = "publications-list.html"