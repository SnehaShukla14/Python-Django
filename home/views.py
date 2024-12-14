# from django.shortcuts import render, HttpResponse

# # Create your views here.
# def index(request):
#     return HttpResponse("this is home page")

# def about(request):
#     return HttpResponse("this is about page")

# def services(request):
#     return HttpResponse("this is services page")

# def contact(request):
#     return HttpResponse("this is contact page")

from rest_framework import viewsets
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

# ViewSet for Clients
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as creator of the client
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['get'])
    def projects(self, request, pk=None):
        client = self.get_object()
        projects = client.projects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

# ViewSet for Projects
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as creator of the project
        serializer.save(created_by=self.request.user)

from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the home page!")





