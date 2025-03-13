from django.urls import path
from .views import PublicationListView, PublicationDetailView # new

urlpatterns = [
    path('',  PublicationListView.as_view(), name='publications-list'),
    path('publication/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail'), # new
]