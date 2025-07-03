from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Campaign
from .serializers import CampaignSerializer

class CampaignView(APIView):
    def get(self, request, pk=None):
        if not pk:
            queryset = Campaign.objects.all()
            serializer = CampaignSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            campaign = get_object_or_404(Campaign, pk=pk)
            serializer = CampaignSerializer(campaign)
            return Response(serializer.data)

    def post(self, request):
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, *args, **kwargs):
        if not pk:
            return Response({"error": "ID is required in the URL"}, status=status.HTTP_400_BAD_REQUEST)
        campaign = get_object_or_404(Campaign, pk=pk)
        serializer = CampaignSerializer(campaign, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, *args, **kwargs):
        if not pk:
            return Response({"error": "ID is required in the URL"}, status=status.HTTP_400_BAD_REQUEST)
        campaign = get_object_or_404(Campaign, pk=pk)
        campaign.delete()
        return Response({"success": "Campaign deleted successfully!"})
