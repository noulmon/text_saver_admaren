from django.urls import path, include
from rest_framework import routers

from .views import TextSnippetViewSet, TagViewSet

router = routers.DefaultRouter()
# router.register('', TextSnippetView)


urlpatterns = [
    path('overview/', TextSnippetViewSet.as_view({'get': 'list'})),
    path('create/', TextSnippetViewSet.as_view({'post': 'create'})),
    path('detail/<int:pk>/', TextSnippetViewSet.as_view({'get': 'retrieve'}), name='textsnippet-detail'),
    path('update/<int:pk>/', TextSnippetViewSet.as_view({'patch': 'partial_update'})),
    path('delete/<int:pk>/', TextSnippetViewSet.as_view({'delete': 'destroy'})),

    path('tag/list/', TagViewSet.as_view({'get': 'list'})),
    path('tag/detail/<int:pk>/', TagViewSet.as_view({'get': 'retrieve'})),
]
