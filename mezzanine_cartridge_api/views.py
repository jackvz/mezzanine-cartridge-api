from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site
from django.contrib.redirects.models import Redirect

from mezzanine.conf.models import Setting
from mezzanine.pages.models import Page

from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.galleries.models import Gallery, GalleryImage

from mezzanine.generic.models import ThreadedComment, AssignedKeyword, Rating

from cartridge.shop.models import Product, ProductImage, ProductOption, ProductVariation, Category, Order, OrderItem, Discount, Sale, DiscountCode

from rest_framework import viewsets
from rest_framework import generics
# from rest_framework import permissions

from rest_framework_api_key.permissions import HasAPIKey, HasAPIKeyOrIsAuthenticated

from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'

class GroupViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


class SiteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


class RedirectViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = Redirect.objects.all()
    serializer_class = RedirectSerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


class SettingViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


class PageViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


class BlogPostViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


class BlogCategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


class GalleryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


class GalleryImageViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


class ThreadedCommentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = ThreadedComment.objects.all()
    serializer_class = ThreadedCommentSerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


class AssignedKeywordViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = AssignedKeyword.objects.all()
    serializer_class = AssignedKeywordSerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


class RatingViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


class ProductImageViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


class ProductOptionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = ProductOption.objects.all()
    serializer_class = ProductOptionSerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


class ProductVariationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = ProductVariation.objects.all()
    serializer_class = ProductVariationSerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


class CategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


class SaleViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'


class DiscountCodeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, update` and `destroy` actions.
    """
    queryset = DiscountCode.objects.all()
    serializer_class = DiscountCodeSerializer
    permission_classes = (HasAPIKeyOrIsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'delete'] # 'patch'
