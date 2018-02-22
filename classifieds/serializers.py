from rest_framework import serializers
from django.contrib.auth.models import User
from classifieds.models import UserProfile, Item, Category, ItemImage, Favorite


class UserSerializer(serializers.ModelSerializer):
    items = serializers.HyperlinkedRelatedField(many=True, view_name='item-detail', read_only=True)

    class Meta:
        model = User 
        fields = ('id', 'email', 'username', 'items')

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = UserProfile
        fields = ('url', 'user', 'id', 'phone', 'description')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.HyperlinkedRelatedField(many=True, view_name='item-detail', read_only=True)
    class Meta:
        model = Category
        fields = ('url', 'id', 'name', 'items')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    category = serializers.PrimaryKeyRelatedField(many=False, queryset=Category.objects.all())

    class Meta:
        model = Item
        fields = ('url', 'id', 'owner', 'title', 'description', 'price', 'category', 'is_active', 'updated', 'posted')

class ItemImageSerializer(serializers.HyperlinkedModelSerializer):
    item = serializers.PrimaryKeyRelatedField(many=False, queryset=Item.objects.all())

    class Meta:
        model = ItemImage
        fields = ('url', 'id', 'item', 'image_id', 'image_version')

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Favorite
        fields = ('id', 'owner', 'item')
