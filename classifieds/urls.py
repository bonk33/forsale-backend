from django.urls import path, include
from classifieds import views
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

swagger_view = get_swagger_view(title='Forsale Classifieds API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'users', views.UserProfileViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'item-images', views.ItemImageViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('authuser', views.GetAuthUser.as_view()),
    path('', include(router.urls)),
    path('docs/', swagger_view),
]
