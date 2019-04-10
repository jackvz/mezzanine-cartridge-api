from django.test import TestCase

from rest_framework import serializers
from mezzanine.conf import settings
from drf_yasg import renderers

from mezzanine_cartridge_api.serializers import *
from mezzanine_cartridge_api.views import *
from mezzanine_cartridge_api.drf_yasg_renderers import *
from mezzanine_cartridge_api.drf_yasg_views import *


# Shared serialiser tests

class SharedSerializerTestsMixin(object):
    def test_serializer(self):
        self.assertEquals(self.Meta.fields, '__all__')

class SharedManyToManyThroughSerializerTestsMixin(object):
    def test_serializer(self):
        pass

class UserSerializerTestCase(UserSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_serializer(self):
        self.assertEquals(self.Meta.exclude, ('user_permissions',))
    def test_model(self):
        self.assertEquals(self.Meta.model, User)

class GroupSerializerTestCase(GroupSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, Group)

class SiteSerializerTestCase(SiteSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, Site)

class RedirectSerializerTestCase(RedirectSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, Redirect)

class SettingSerializerTestCase(SettingSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, Setting)

class PageSerializerTestCase(PageSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, Page)

class BlogPostSerializerTestCase(BlogPostSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, BlogPost)

class BlogCategorySerializerTestCase(BlogCategorySerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, BlogCategory)

class GallerySerializerTestCase(GallerySerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, Gallery)

class GalleryImageSerializerTestCase(GalleryImageSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, GalleryImage)

class ThreadedCommentSerializerTestCase(ThreadedCommentSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, ThreadedComment)

class AssignedKeywordSerializerTestCase(AssignedKeywordSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, AssignedKeyword)

class RatingSerializerTestCase(RatingSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, Rating)

class ProductProductManyToManyThroughSerializerTestCase(ProductProductManyToManyThroughSerializer, TestCase, SharedManyToManyThroughSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, Product)
        self.assertEquals(self.Meta.exclude, ('categories', 'related_products', 'upsell_products'));

class ProductSerializerTestCase(ProductSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, Product)

class ProductImageSerializerTestCase(ProductImageSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, ProductImage)

class ProductOptionSerializerTestCase(ProductOptionSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, ProductOption)

class ProductVariationSerializerTestCase(ProductVariationSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, ProductVariation)

class CategoryProductManyToManyThroughSerializerTestCase(CategoryProductManyToManyThroughSerializer, TestCase, SharedManyToManyThroughSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, Product)
        self.assertEquals(self.Meta.exclude, ('categories', 'related_products', 'upsell_products'));

class CategorySerializerTestCase(CategorySerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, Category)

class CartSerializerTestCase(CartSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, Cart)

class CartItemSerializerTestCase(CartItemSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, CartItem)

class OrderSerializerTestCase(OrderSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, Order)

class OrderItemSerializerTestCase(OrderItemSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, OrderItem)

class SaleSerializerTestCase(SaleSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, Sale)

class DiscountCodeSerializerTestCase(DiscountCodeSerializer, TestCase, SharedSerializerTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
    def test_model(self):
        self.assertEquals(self.Meta.model, DiscountCode)

# Shared view tests

class SharedViewTestsMixin(object):
    def test_view(self):
         self.assertEquals(self.permission_classes, (HasAPIKey,))
         self.assertEquals(self.http_method_names, ['head', 'get', 'post', 'put', 'patch', 'delete'])
         self.assertEquals(self.paginator, None)

class UserViewSetTestCase(UserViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class GroupViewSetTestCase(GroupViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class SiteViewSetTestCase(SiteViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class RedirectViewSetTestCase(RedirectViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class SettingViewSetTestCase(SettingViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class PageViewSetTestCase(PageViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class BlogPostViewSetTestCase(BlogPostViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class BlogCategoryViewSetTestCase(BlogCategoryViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class GalleryViewSetTestCase(GalleryViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class GalleryImageViewSetTestCase(GalleryImageViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class ThreadedCommentViewSetTestCase(ThreadedCommentViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class AssignedKeywordViewSetTestCase(AssignedKeywordViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class RatingViewSetTestCase(RatingViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class ProductViewSetTestCase(ProductViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class ProductImageViewSetTestCase(ProductImageViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class ProductOptionViewSetTestCase(ProductOptionViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class ProductVariationViewSetTestCase(ProductVariationViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class CategoryViewSetTestCase(CategoryViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class CartViewSetTestCase(CartViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class CartItemViewSetTestCase(CartItemViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class OrderViewSetTestCase(OrderViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class OrderItemViewSetTestCase(OrderItemViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class SaleViewSetTestCase(SaleViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

class DiscountCodeViewSetTestCase(DiscountCodeViewSet, TestCase, SharedViewTestsMixin):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

# Generic tests

class MezzanineCartridgeApiTestCase(TestCase):
    def test_config(self):
        self.assertEqual(settings.CORS_ORIGIN_ALLOW_ALL, True)

        self.assertEqual(settings.REST_FRAMEWORK, {
            'PAGE_SIZE': 10,
            'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
            'DEFAULT_AUTHENTICATION_CLASSES': (
                # 'rest_framework.authentication.BasicAuthentication',
                'rest_framework.authentication.SessionAuthentication',
                # 'rest_framework.authentication.TokenAuthentication',
                # 'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
            ),
            'DEFAULT_PERMISSION_CLASSES': (
                'rest_framework.permissions.IsAuthenticated',
                'rest_framework_api_key.permissions.HasAPIKey',
            ),
        })

        self.assertEqual(settings.SWAGGER_SETTINGS, {
            'LOGIN_URL': '/admin/login/',
            'LOGOUT_URL': '/admin/logout/',
            'DOC_EXPANSION': 'list',
            'USE_SESSION_AUTH': False,
            'APIS_SORTER': 'alpha',
            'SECURITY_DEFINITIONS': {
                "API Token": {
                    "type": "apiKey",
                    "name": "Api-Token",
                    "in": "header"
                },
                "API Secret Key": {
                    "type": "apiKey",
                    "name": "Api-Secret-Key",
                    "in": "header"
                },
            }
        })

        self.assertEqual(settings.SWAGGER_SCHEME_HTTPS, False)

    def test_swagger_renderer(self):
        self.assertEqual(SwaggerUIRendererWithAllSchemes.template, 'swagger-ui-all-schemes.html')

