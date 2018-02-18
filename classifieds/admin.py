from django.contrib import admin
from classifieds.models import UserProfile, Item, Category, ItemImage

class ItemImageAdminInline(admin.TabularInline):
    model = ItemImage

class ItemAdmin(admin.ModelAdmin):
    inlines = (ItemImageAdminInline, )

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(ItemImage)
