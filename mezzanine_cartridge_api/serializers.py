from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site
from django.contrib.redirects.models import Redirect

from mezzanine.conf.models import Setting
from mezzanine.pages.models import Page

from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.galleries.models import Gallery, GalleryImage

from mezzanine.generic.models import ThreadedComment, AssignedKeyword, Rating

# Conditionally include Cartridge models, if the Cartridge package is installed
try:
    from cartridge.shop.models import Product, ProductImage, ProductOption, ProductVariation, Category, Order, OrderItem, Discount, Sale, DiscountCode
except:
    pass

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = '__all__'

class UserPasswordCheckSerializer(serializers.Serializer):
    email_or_username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class UserTokenCheckSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)

class UserActivationSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)

class UserPasswordSetSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Group
        fields = '__all__'

class SiteSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Site
        fields = '__all__'

class RedirectSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Redirect
        fields = '__all__'

class SettingSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Setting
        fields = '__all__'

class PageSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Page
        fields = '__all__'

class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = BlogPost
        fields = '__all__'

class BlogCategorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = BlogCategory
        fields = '__all__'


class GallerySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Gallery
        fields = '__all__'


class GalleryImageSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = GalleryImage
        fields = '__all__'


class ThreadedCommentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = ThreadedComment
        fields = '__all__'


class AssignedKeywordSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = AssignedKeyword
        fields = '__all__'


class RatingSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Rating
        fields = '__all__'


# Conditionally include Cartridge models, if the Cartridge package is installed
try:
    class ProductSerializer(serializers.HyperlinkedModelSerializer):
        id = serializers.ReadOnlyField()
        class Meta:
            model = Product
            fields = '__all__'


    class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
        id = serializers.ReadOnlyField()
        class Meta:
            model = ProductImage
            fields = '__all__'


    class ProductOptionSerializer(serializers.HyperlinkedModelSerializer):
        id = serializers.ReadOnlyField()
        class Meta:
            model = ProductOption
            fields = '__all__'


    class ProductVariationSerializer(serializers.HyperlinkedModelSerializer):
        id = serializers.ReadOnlyField()
        class Meta:
            model = ProductVariation
            fields = '__all__'


    class CategorySerializer(serializers.HyperlinkedModelSerializer):
        id = serializers.ReadOnlyField()
        class Meta:
            model = Category
            fields = '__all__'


    class OrderSerializer(serializers.HyperlinkedModelSerializer):
        id = serializers.ReadOnlyField()
        class Meta:
            model = Order
            fields = '__all__'


    class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
        id = serializers.ReadOnlyField()
        class Meta:
            model = OrderItem
            fields = '__all__'


    class SaleSerializer(serializers.HyperlinkedModelSerializer):
        id = serializers.ReadOnlyField()
        class Meta:
            model = Sale
            fields = '__all__'


    class DiscountCodeSerializer(serializers.HyperlinkedModelSerializer):
        id = serializers.ReadOnlyField()
        class Meta:
            model = DiscountCode
            fields = '__all__'
except:
    pass
