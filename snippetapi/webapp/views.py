from django.shortcuts import render
from .models import Snippet, Tag
from django.http import HttpResponse, JsonResponse
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics
from .permissions import IsOwnerOrReadOnly
# Create your views here.
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'overview': reverse('overview-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
        'tags': reverse('tag-list', request=request, format=format),
        
    })


class OverViewApi(generics.ListAPIView):
    queryset = Snippet.objects.select_related('tag').all()
    serializer_class = SnippetoverviewSerializer
    authentication_classes = ([JWTAuthentication])
    permission_classes = ([IsAuthenticated])

class SnippetListView(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetPostSerializer
    authentication_classes = ([JWTAuthentication])
    permission_classes = ([IsAuthenticated])

    def perform_create(self, serializer):
        serializer.save(created_user_id=self.request.user)


class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetPostSerializer
    authentication_classes = ([JWTAuthentication])
    permission_classes = ([IsAuthenticated,IsOwnerOrReadOnly])

    def perform_create(self, serializer):
        serializer.save(created_user=self.request.user)

class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = ([JWTAuthentication])
    permission_classes = ([IsAuthenticated])

class TagDetailsView(generics.ListAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetPostSerializer
    authentication_classes = ([JWTAuthentication])
    permission_classes = ([IsAuthenticated])

    def get_queryset(request):
        return Snippet.objects.filter(tag=request.kwargs['pk'])
