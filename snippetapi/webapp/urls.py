from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('overview/', views.OverViewApi.as_view(), name = 'overview-list'),
    path('snippets/<int:pk>/', views.SnippetDetailView.as_view(), name = 'snippet-detail'),
    path('snippets/', views.SnippetListView.as_view(), name = 'snippet-list'),
    path('tags/', views.TagListView.as_view(), name = 'tag-list'),
    path('tags/<int:pk>/', views.TagDetailsView.as_view(), name = 'tag-detail'),
    path('', views.api_root),
    
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
])