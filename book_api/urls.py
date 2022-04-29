from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from books.views import BookViewSet, AuthorViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('', include(router.urls))
]
