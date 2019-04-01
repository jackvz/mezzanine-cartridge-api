from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site
from django.contrib.redirects.models import Redirect
from django.utils.decorators import method_decorator

from mezzanine.conf.models import Setting
from mezzanine.pages.models import Page

from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.galleries.models import Gallery, GalleryImage

from mezzanine.generic.models import ThreadedComment, AssignedKeyword, Rating

# Conditionally include Cartridge viewsets, if the Cartridge package is installed
try:
    from cartridge.shop.models import Product, ProductImage, ProductOption, ProductVariation, Category, Order, OrderItem, Discount, Sale, DiscountCode
except:
    pass

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework_api_key.permissions import HasAPIKey, HasAPIKeyOrIsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from .serializers import *


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
class UserViewSet(viewsets.ModelViewSet, APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'

@method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
class RedirectViewSet(viewsets.ModelViewSet):
    queryset = Redirect.objects.all()
    serializer_class = RedirectSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
class SettingViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
class ThreadedCommentViewSet(viewsets.ModelViewSet):
    queryset = ThreadedComment.objects.all()
    serializer_class = ThreadedCommentSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
class AssignedKeywordViewSet(viewsets.ModelViewSet):
    queryset = AssignedKeyword.objects.all()
    serializer_class = AssignedKeywordSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (HasAPIKey,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'

# Conditionally include Cartridge viewsets, if the Cartridge package is installed
try:
    @method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
    @method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
    @method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
    class ProductViewSet(viewsets.ModelViewSet):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        permission_classes = (HasAPIKey,)
        http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


    @method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
    @method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
    @method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
    class ProductImageViewSet(viewsets.ModelViewSet):
        queryset = ProductImage.objects.all()
        serializer_class = ProductImageSerializer
        permission_classes = (HasAPIKey,)
        http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


    @method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
    @method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
    @method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
    class ProductOptionViewSet(viewsets.ModelViewSet):
        queryset = ProductOption.objects.all()
        serializer_class = ProductOptionSerializer
        permission_classes = (HasAPIKey,)
        http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


    @method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
    @method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
    @method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
    class ProductVariationViewSet(viewsets.ModelViewSet):
        queryset = ProductVariation.objects.all()
        serializer_class = ProductVariationSerializer
        permission_classes = (HasAPIKey,)
        http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


    @method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
    @method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
    @method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
    class CategoryViewSet(viewsets.ModelViewSet):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
        permission_classes = (HasAPIKey,)
        http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


    @method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
    @method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
    @method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
    class OrderViewSet(viewsets.ModelViewSet):
        queryset = Order.objects.all()
        serializer_class = OrderSerializer
        permission_classes = (HasAPIKey,)
        http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


    @method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
    @method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
    @method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
    class OrderItemViewSet(viewsets.ModelViewSet):
        queryset = OrderItem.objects.all()
        serializer_class = OrderItemSerializer
        permission_classes = (HasAPIKey,)
        http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


    @method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
    @method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
    @method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
    class SaleViewSet(viewsets.ModelViewSet):
        queryset = Sale.objects.all()
        serializer_class = SaleSerializer
        permission_classes = (HasAPIKey,)
        http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


    @method_decorator(name='list', decorator=swagger_auto_schema(operation_description="List all",))
    @method_decorator(name='create', decorator=swagger_auto_schema(operation_description="Create",))
    @method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description="Retrieve",))
    @method_decorator(name='update', decorator=swagger_auto_schema(operation_description="Update",))
    @method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description="Destroy",))
    class DiscountCodeViewSet(viewsets.ModelViewSet):
        queryset = DiscountCode.objects.all()
        serializer_class = DiscountCodeSerializer
        permission_classes = (HasAPIKey,)
        http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'
except:
    pass
