from django.urls import path

from .views import CampaignView

urlpatterns = [
    # list and create
    path('campaign/nt/', CampaignView.as_view(), name='campaign-list'),
    # retrieve, update, delete
    path('campaign/<int:pk>/nt/', CampaignView.as_view(), name='campaign-detail'),
]