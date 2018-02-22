import graphene 
from graphene_django.types import DjangoObjectType

from django.contrib.auth.models import User
from classifieds.models import UserProfile, Item, Category, ItemImage, Favorite

class UserType(DjangoObjectType):
    class Meta:
        model = User

class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile

class CategoryType(DjangoObjectType):
    class Meta: 
        model = Category

class ItemType(DjangoObjectType):
    class Meta: 
        model = Item

class ItemImageType(DjangoObjectType):
    class Meta:
        model = ItemImage

class FavoriteType(DjangoObjectType):
    class Meta:
        model = Favorite

class Query(object):
    user = graphene.Field(UserType, id=graphene.Int())
    user_profile = graphene.Field(UserProfileType, id=graphene.Int())
    all_userProfiles= graphene.List(UserProfileType)

    category = graphene.Field(CategoryType, id=graphene.Int())
    all_categories = graphene.List(CategoryType)

    item = graphene.Field(ItemType, id=graphene.Int())
    all_items = graphene.List(ItemType)

    item_image = graphene.Field(ItemImageType, id=graphene.Int())
    
    favorite = graphene.Field(FavoriteType, id=graphene.Int())

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return User.objects.get(pk=id) 
    
    def resolve_all_userProfiles(self, info, **kwargs):
        return UserProfile.objects.all()
    
    def resolve_user_profile(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return UserProfile.objects.get(pk=id)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Category.objects.get(pk=id)


    def resolve_all_items(self, info, **kwargs):
        return Item.objects.all()
    
    def resolve_item(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Item.objects.get(pk=id)

