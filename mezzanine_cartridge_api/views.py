from django.contrib.auth import authenticate
from django.contrib.auth.tokens import default_token_generator

from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site
from django.contrib.redirects.models import Redirect

from django.http import HttpRequest

from django.utils.decorators import method_decorator

from mezzanine.conf.models import Setting
from mezzanine.pages.models import Page

from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.galleries.models import Gallery, GalleryImage

from mezzanine.generic.models import ThreadedComment, AssignedKeyword, Rating

# Conditionally include Cartridge viewsets, if the Cartridge package is installed
try:
    from cartridge.shop.models import Product, ProductImage, ProductOption, ProductVariation, Category, Cart, CartItem, Order, OrderItem, Discount, Sale, DiscountCode
except:
    pass

import json

from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_framework_api_key.permissions import HasAPIKey, HasAPIKeyOrIsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from django.conf import settings as django_settings
from mezzanine.conf import settings
from mezzanine.utils.importing import import_dotted_path

from .serializers import *


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
class SystemSettingViewSet(viewsets.GenericViewSet, viewsets.mixins.ListModelMixin):
    serializer_class = SystemSettingSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get']
    paginator = None
    def get_queryset(self):
        system_settings = []
        for attr in dir(django_settings):
            if attr.isupper() and attr != 'DATABASES':
                system_setting = SystemSetting()
                system_setting.name = attr
                system_setting.value = getattr(settings, attr)
                system_settings.append(system_setting)
        return system_settings


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
@method_decorator(name='check_password', decorator=swagger_auto_schema(operation_description='Check password', request_body=UserPasswordCheckSerializer))
@method_decorator(name='check_token', decorator=swagger_auto_schema(operation_description='Check token', request_body=UserTokenCheckSerializer))
@method_decorator(name='activate', decorator=swagger_auto_schema(operation_description='Activate', request_body=UserActivationSerializer))
@method_decorator(name='set_password', decorator=swagger_auto_schema(operation_description='Set password', request_body=UserPasswordSetSerializer))
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
    paginator = None

    @action(serializer_class=UserPasswordCheckSerializer, methods=['post'], detail=False, permission_classes=(HasAPIKey,), url_path='check-password')
    def check_password(self, request):
        serializer = UserPasswordCheckSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if not authenticate(username=serializer.data.get('email_or_username'), password=serializer.data.get('password')):
            return Response({'status': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'Valid credentials'}, status=status.HTTP_200_OK)

    @action(serializer_class=UserTokenCheckSerializer, methods=['post'], detail=True, permission_classes=(HasAPIKey,), url_path='check-token')
    def check_token(self, request, pk):
        serializer = UserTokenCheckSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(id=pk)
        except:
            return Response({'detail': ['Not found.']}, status=status.HTTP_404_NOT_FOUND)
        if not default_token_generator.check_token(user, serializer.data.get('token')):
            return Response({'token': ['Invalid token.']}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'Valid token'}, status=status.HTTP_200_OK)

    @action(serializer_class=UserActivationSerializer, methods=['post'], detail=True, permission_classes=(HasAPIKey,), url_path='activate')
    def activate(self, request, pk):
        serializer = UserActivationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(id=pk)
        except:
            return Response({'detail': ['Not found.']}, status=status.HTTP_404_NOT_FOUND)
        if not default_token_generator.check_token(user, serializer.data.get('token')):
            return Response({'token': ['Invalid token.']}, status=status.HTTP_400_BAD_REQUEST)
        user.is_active = True
        user.save()
        return Response({'status': 'User activated'}, status=status.HTTP_200_OK)

    @action(serializer_class=UserPasswordSetSerializer, methods=['post'], detail=True, permission_classes=(HasAPIKey,), url_path='set-password')
    def set_password(self, request, pk):
        serializer = UserPasswordSetSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(id=pk)
        except:
            return Response({'detail': ['Not found.']}, status=status.HTTP_404_NOT_FOUND)
        if not user.check_password(serializer.data.get('old_password')):
            return Response({'old_password': ['Wrong password.']}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(serializer.data.get('new_password'))
        user.save()
        return Response({'status': 'Password set'}, status=status.HTTP_200_OK)


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
    paginator = None


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
    paginator = None


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
class RedirectViewSet(viewsets.ModelViewSet):
    queryset = Redirect.objects.all()
    serializer_class = RedirectSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
    paginator = None


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
class SettingViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
    paginator = None


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
    paginator = None


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
    paginator = None


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
    paginator = None


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
    paginator = None


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
    paginator = None


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
class ThreadedCommentViewSet(viewsets.ModelViewSet):
    queryset = ThreadedComment.objects.all()
    serializer_class = ThreadedCommentSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
    paginator = None


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
class AssignedKeywordViewSet(viewsets.ModelViewSet):
    queryset = AssignedKeyword.objects.all()
    serializer_class = AssignedKeywordSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
    paginator = None


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
    paginator = None

# Conditionally include Cartridge viewsets, if the Cartridge package is installed
try:
    @method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
    @method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
    @method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
    @method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
    class ProductViewSet(viewsets.ModelViewSet):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        permission_classes = (HasAPIKey,)
        http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
        paginator = None


    @method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
    @method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
    @method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
    @method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
    class ProductImageViewSet(viewsets.ModelViewSet):
        queryset = ProductImage.objects.all()
        serializer_class = ProductImageSerializer
        permission_classes = (HasAPIKey,)
        http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
        paginator = None


    @method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
    @method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
    @method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
    @method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
    class ProductOptionViewSet(viewsets.ModelViewSet):
        queryset = ProductOption.objects.all()
        serializer_class = ProductOptionSerializer
        permission_classes = (HasAPIKey,)
        http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
        paginator = None


    @method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
    @method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
    @method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
    @method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
    class ProductVariationViewSet(viewsets.ModelViewSet):
        queryset = ProductVariation.objects.all()
        serializer_class = ProductVariationSerializer
        permission_classes = (HasAPIKey,)
        http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
        paginator = None


    @method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
    @method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
    @method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
    @method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
    class CategoryViewSet(viewsets.ModelViewSet):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
        permission_classes = (HasAPIKey,)
        http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
        paginator = None


    @method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
    @method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
    @method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
    @method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
    @method_decorator(name='billing_shipping', decorator=swagger_auto_schema(operation_description='Execute billing/shipping handler', request_body=CartBillingShippingSerializer))
    @method_decorator(name='tax', decorator=swagger_auto_schema(operation_description='Execute tax handler', request_body=CartTaxSerializer))
    @method_decorator(name='payment', decorator=swagger_auto_schema(operation_description='Execute payment handler', request_body=CartPaymentSerializer))
    @method_decorator(name='order_placement', decorator=swagger_auto_schema(operation_description='Execute order placement handler', request_body=OrderPlacementSerializer))
    class CartViewSet(viewsets.ModelViewSet):
        queryset = Cart.objects.all()
        serializer_class = CartSerializer
        permission_classes = (HasAPIKey,)
        http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
        paginator = None

        @action(serializer_class=CartBillingShippingSerializer, methods=['post'], detail=True, permission_classes=(HasAPIKey,), url_path='billing-shipping')
        def billing_shipping(self, request, pk):
            serializer = CartBillingShippingSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            try:
                cart = Cart.objects.get(id=pk)
            except:
                return Response({'detail': ['Not found.']}, status=status.HTTP_404_NOT_FOUND)
            handler = lambda s: import_dotted_path(s) if s else lambda *args: None
            billship_handler = handler(settings.SHOP_HANDLER_BILLING_SHIPPING)
            request_front = HttpRequest()
            request_front.session = serializer.data.get('additional_session_items')
            request_front.session['cart'] = pk
            request_front.cart = cart
            billship_handler(request_front, None)
            return Response({'status': 'Billing/Shipping handler executed', 'session': json.dumps(request_front.session)}, status=status.HTTP_200_OK)

        @action(serializer_class=CartTaxSerializer, methods=['post'], detail=True, permission_classes=(HasAPIKey,), url_path='tax')
        def tax(self, request, pk):
            serializer = CartTaxSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            try:
                cart = Cart.objects.get(id=pk)
                order = Order.objects.get(id=serializer.data.get('order_id'))
            except:
                return Response({'detail': ['Not found.']}, status=status.HTTP_404_NOT_FOUND)
            handler = lambda s: import_dotted_path(s) if s else lambda *args: None
            tax_handler = handler(settings.SHOP_HANDLER_TAX)
            request_front = HttpRequest()
            request_front.session = serializer.data.get('additional_session_items')
            request_front.session['cart'] = pk
            request_front.cart = cart
            tax_handler(request_front, None)
            return Response({'status': 'Tax handler executed', 'session': json.dumps(request_front.session)}, status=status.HTTP_200_OK)

        @action(serializer_class=CartPaymentSerializer, methods=['post'], detail=True, permission_classes=(HasAPIKey,), url_path='payment')
        def payment(self, request, pk):
            serializer = CartPaymentSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            try:
                cart = Cart.objects.get(id=pk)
                order = Order.objects.get(id=serializer.data.get('order_id'))
            except:
                return Response({'detail': ['Not found.']}, status=status.HTTP_404_NOT_FOUND)
            handler = lambda s: import_dotted_path(s) if s else lambda *args: None
            payment_handler = handler(settings.SHOP_HANDLER_PAYMENT)
            request_front = HttpRequest()
            request_front.session = serializer.data.get('additional_session_items')
            request_front.session['cart'] = pk
            request_front.cart = cart
            payment_handler(request_front, order, order)
            return Response({'status': 'Payment handler executed', 'session': json.dumps(request_front.session)}, status=status.HTTP_200_OK)

        @action(serializer_class=OrderPlacementSerializer, methods=['post'], detail=True, permission_classes=(HasAPIKey,), url_path='order-placement')
        def order_placement(self, request, pk):
            serializer = OrderPlacementSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            try:
                cart = Cart.objects.get(id=pk)
                order = Order.objects.get(id=serializer.data.get('order_id'))
            except:
                return Response({'detail': ['Not found.']}, status=status.HTTP_404_NOT_FOUND)
            handler = lambda s: import_dotted_path(s) if s else lambda *args: None
            order_handler = handler(settings.SHOP_HANDLER_ORDER)
            request_front = HttpRequest()
            request_front.session = serializer.data.get('additional_session_items')
            request_front.session['cart'] = pk
            request_front.cart = cart
            order_handler(request_front, order, order)
            return Response({'status': 'Order placement handler executed', 'session': json.dumps(request_front.session)}, status=status.HTTP_200_OK)


    @method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
    @method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
    @method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
    @method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
    class CartItemViewSet(viewsets.ModelViewSet):
        queryset = CartItem.objects.all()
        serializer_class = CartItemSerializer
        permission_classes = (HasAPIKey,)
        http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
        paginator = None


    @method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
    @method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
    @method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
    @method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
    class OrderViewSet(viewsets.ModelViewSet):
        queryset = Order.objects.all()
        serializer_class = OrderSerializer
        permission_classes = (HasAPIKey,)
        http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
        paginator = None


    @method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
    @method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
    @method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
    @method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
    class OrderItemViewSet(viewsets.ModelViewSet):
        queryset = OrderItem.objects.all()
        serializer_class = OrderItemSerializer
        permission_classes = (HasAPIKey,)
        http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
        paginator = None


    @method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
    @method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
    @method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
    @method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
    class SaleViewSet(viewsets.ModelViewSet):
        queryset = Sale.objects.all()
        serializer_class = SaleSerializer
        permission_classes = (HasAPIKey,)
        http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
        paginator = None


    @method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List all',))
    @method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create',))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Retrieve',))
    @method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update',))
    @method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_description='Partial update',))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Destroy',))
    class DiscountCodeViewSet(viewsets.ModelViewSet):
        queryset = DiscountCode.objects.all()
        serializer_class = DiscountCodeSerializer
        permission_classes = (HasAPIKey,)
        http_method_names = ['head', 'get', 'post', 'put', 'patch', 'delete']
        paginator = None
except:
    pass
