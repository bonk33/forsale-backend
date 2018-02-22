from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from classifieds.models import UserProfile, Item, Category, ItemImage, Favorite

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomsUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomsUserAdmin, self).get_inline_instances(request, obj)

class ItemImageAdminInline(admin.TabularInline):
    model = ItemImage

class ItemAdmin(admin.ModelAdmin):
    inlines = (ItemImageAdminInline, )

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, CustomsUserAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(ItemImage)
admin.site.register(Favorite)
