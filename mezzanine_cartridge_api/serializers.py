from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site
from django.contrib.redirects.models import Redirect
from django import forms
from django.conf import settings as django_settings
from enum import Enum

from drf_braces.serializers.form_serializer import FormSerializer
from enumfields import EnumIntegerField

from mezzanine.conf.models import Setting
from mezzanine.pages.models import Page

from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.galleries.models import Gallery, GalleryImage

from mezzanine.generic.models import ThreadedComment, AssignedKeyword, Rating

# Conditionally include Cartridge models, if the Cartridge package is installed
try:
    from cartridge.shop.models import Product, ProductImage, ProductOption, ProductVariation, Category, Cart, CartItem, Order, OrderItem, Discount, Sale, DiscountCode
    from cartridge.shop.forms import OrderForm
except:
    pass

from rest_framework import serializers

from .fields import *
from .models import *


# Serializer for in-memory Django/Mezzanine settings
class SystemSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetting
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Group
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    groups = GroupSerializer(many=True, read_only=True)
    class Meta:
        model = User
        exclude = ('user_permissions',)

class UserPasswordCheckSerializer(serializers.Serializer):
    email_or_username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class UserTokenCheckSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)

class UserActivationSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)

class UserPasswordResetSerializer(serializers.Serializer):
    email_or_username = serializers.CharField(required=True)

class UserPasswordSetSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class SiteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Site
        fields = '__all__'


class RedirectSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Redirect
        fields = '__all__'


class SettingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Setting
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Page
        fields = '__all__'


class BlogCategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = BlogCategory
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    categories = BlogCategorySerializer(many=True, read_only=True)
    class Meta:
        model = BlogPost
        fields = '__all__'


class GalleryImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = GalleryImage
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    images = GalleryImageSerializer(many=True, read_only=True)
    class Meta:
        model = Gallery
        fields = '__all__'


class ThreadedCommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = ThreadedComment
        fields = '__all__'


class AssignedKeywordSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = AssignedKeyword
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Rating
        fields = '__all__'


# Conditionally include Cartridge models, if the Cartridge package is installed
try:
    class CategoryProductManyToManyThroughSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField(read_only=True)
        class Meta:
            model = Product
            exclude = ('categories', 'related_products', 'upsell_products')


    class ProductOptionSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField(read_only=True)
        class Meta:
            model = ProductOption
            fields = '__all__'


    class CategorySerializer(serializers.ModelSerializer):
        id = serializers.IntegerField(read_only=True)
        products = CategoryProductManyToManyThroughSerializer(many=True, read_only=True)
        options = ProductOptionSerializer(many=True, read_only=True)
        class Meta:
            model = Category
            fields = '__all__'


    class ProductImageSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField(read_only=True)
        class Meta:
            model = ProductImage
            fields = '__all__'


    class ProductVariationSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField(read_only=True)
        class Meta:
            model = ProductVariation
            fields = '__all__'


    class ProductProductManyToManyThroughSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField(read_only=True)
        class Meta:
            model = Product
            exclude = ('categories', 'related_products', 'upsell_products')


    class ProductSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField(read_only=True)
        images = ProductImageSerializer(many=True, read_only=True)
        variations = ProductVariationSerializer(many=True, read_only=True)
        categories = CategorySerializer(many=True, read_only=True)
        related_products = ProductProductManyToManyThroughSerializer(many=True, read_only=True)
        upsell_products = ProductProductManyToManyThroughSerializer(many=True, read_only=True)
        class Meta:
            model = Product
            fields = '__all__'


    # Form for Cartridge orders
    class CheckoutForm(OrderForm):
        # class OneStepType(Enum):
        #     CHECKOUT = 1
        # class TwoStepsType(Enum):
        #     ADDRESS = 1
        #     PAYMENT = 2
        # class OneStepWithConfirmationType(Enum):
        #     CHECKOUT = 1
        #     CONFIRMATION = 2
        # class TwoStepsWithConfirmationType(Enum):
        #     ADDRESS = 1
        #     PAYMENT = 2
        #     CONFIRMATION = 3
        # step = EnumIntegerField(enum=OneStepType) # Override the step field (int) with an enum
        # # SHOP_CHECKOUT_STEPS_SPLIT, SHOP_CHECKOUT_STEPS_CONFIRMATION and SHOP_CHECKOUT_STEPS_SPLIT defaults to true, so check if these either don't exist or are set to true.
        # if (not hasattr(django_settings, 'SHOP_CHECKOUT_STEPS_SPLIT') or django_settings.SHOP_CHECKOUT_STEPS_SPLIT) and (not hasattr(django_settings, 'SHOP_PAYMENT_STEP_ENABLED') or django_settings.SHOP_PAYMENT_STEP_ENABLED):
        #     step = EnumIntegerField(enum=TwoStepsType)
        # if (not hasattr(django_settings, 'SHOP_CHECKOUT_STEPS_CONFIRMATION') or django_settings.SHOP_CHECKOUT_STEPS_CONFIRMATION):
        #     step = EnumIntegerField(enum=OneStepWithConfirmationType)
        #     if (not hasattr(django_settings, 'SHOP_CHECKOUT_STEPS_SPLIT') or django_settings.SHOP_CHECKOUT_STEPS_SPLIT) and (not hasattr(django_settings, 'SHOP_PAYMENT_STEP_ENABLED') or django_settings.SHOP_PAYMENT_STEP_ENABLED):
        #         step = EnumIntegerField(enum=TwoStepsWithConfirmationType)
        step = forms.IntegerField() # Override the step field, to disable validation; @todo: This can be cleaned up when there is time
        card_expiry_year = forms.IntegerField() # Override the card_expiry_year field (choice) with an int, to disable validation; @todo: This can be cleaned up when there is time



    class OrderFormSerializer(FormSerializer):
        # step = EnumField(enum=CheckoutForm.OneStepType)
        # # SHOP_CHECKOUT_STEPS_SPLIT, SHOP_CHECKOUT_STEPS_CONFIRMATION and SHOP_CHECKOUT_STEPS_SPLIT defaults to true, so check if these either don't exist or are set to true.
        # if (not hasattr(django_settings, 'SHOP_CHECKOUT_STEPS_SPLIT') or django_settings.SHOP_CHECKOUT_STEPS_SPLIT) and (not hasattr(django_settings, 'SHOP_PAYMENT_STEP_ENABLED') or django_settings.SHOP_PAYMENT_STEP_ENABLED):
        #     step = EnumField(enum=CheckoutForm.TwoStepsType)
        # if (not hasattr(django_settings, 'SHOP_CHECKOUT_STEPS_CONFIRMATION') or django_settings.SHOP_CHECKOUT_STEPS_CONFIRMATION):
        #     step = EnumField(enum=CheckoutForm.OneStepWithConfirmationType)
        #     if (not hasattr(django_settings, 'SHOP_CHECKOUT_STEPS_SPLIT') or django_settings.SHOP_CHECKOUT_STEPS_SPLIT) and (not hasattr(django_settings, 'SHOP_PAYMENT_STEP_ENABLED') or django_settings.SHOP_PAYMENT_STEP_ENABLED):
        #         step = EnumField(enum=CheckoutForm.TwoStepsWithConfirmationType)
        class Meta(object):
            form = CheckoutForm
            fields = '__all__'


    class CartItemSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField(read_only=True)
        class Meta:
            model = CartItem
            fields = '__all__'


    class CartSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField(read_only=True)
        items = CartItemSerializer(many=True, read_only=True)
        class Meta:
            model = Cart
            fields = '__all__'

    class CartBillingShippingSerializer(serializers.Serializer):
        form = OrderFormSerializer(many=False)
        additional_session_items = serializers.DictField(required=False)

    class CartTaxSerializer(serializers.Serializer):
        form = OrderFormSerializer(many=False)
        order_id = serializers.IntegerField(required=False)
        additional_session_items = serializers.DictField(required=False)

    class CartPaymentSerializer(serializers.Serializer):
        form = OrderFormSerializer(many=False)
        order_id = serializers.IntegerField(required=False)
        additional_session_items = serializers.DictField(required=False)

    class OrderPlacementSerializer(serializers.Serializer):
        form = OrderFormSerializer(many=False)
        order_id = serializers.IntegerField(required=False)
        additional_session_items = serializers.DictField(required=False)


    class OrderItemSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField(read_only=True)
        class Meta:
            model = OrderItem
            fields = '__all__'


    class OrderSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField(read_only=True)
        items = OrderItemSerializer(many=True, read_only=True)
        class Meta:
            model = Order
            fields = '__all__'


    class SaleSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField(read_only=True)
        class Meta:
            model = Sale
            fields = '__all__'


    class DiscountCodeSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField(read_only=True)
        class Meta:
            model = DiscountCode
            fields = '__all__'
except:
    pass
