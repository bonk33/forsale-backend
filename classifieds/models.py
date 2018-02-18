from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('category')
        verbose_name_plural = ('categories')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Item(models.Model):
    slug = models.SlugField(blank=True, null=True, max_length=100)
    owner = models.ForeignKey('auth.User', related_name='items', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='category', related_name='items', on_delete=None)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('item')
        verbose_name_plural = ('items')
        ordering = ('-updated', )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Item, self).save(*args, **kwargs)

class ItemImage(models.Model):
    image_id = models.CharField(max_length=200)
    image_version = models.CharField(max_length=100)
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Item image')
        verbose_name_plural = ('Item images')

class Favorite(models.Model):
    owner = models.ForeignKey('auth.User', related_name='favorites', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='favorites', on_delete=None)
