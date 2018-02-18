from classifieds.models import Item, Category, UserProfile, ItemImage
from classifieds.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from classifieds.serializers import ItemSerializer, UserProfileSerializer, CategorySerializer, ItemImageSerializer
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.views import APIView

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'items': reverse('item-list', request=request, format=format)
    })

class GetAuthUser(APIView):
    """
    This endpoint returns the currently authenticated user
    """
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user, context={'request': request})
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset= Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List of Users and details of Users
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAdminUser, IsOwnerOrReadOnly)

class ItemViewSet(viewsets.ModelViewSet):
    """
    You can `list`, `update`, `retrieve`, and `delete` items with this views
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ItemImageViewSet(viewsets.ModelViewSet):
    queryset = ItemImage.objects.all()
    serializer_class = ItemImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
