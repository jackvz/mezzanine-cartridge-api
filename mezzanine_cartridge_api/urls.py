from django.conf.urls import include, url
from django.views.generic.base import RedirectView

from rest_framework import routers

from rest_framework import permissions

from drf_yasg.renderers import ReDocRenderer, ReDocOldRenderer
from .drf_yasg_renderers import *
# from drf_yasg.views import get_schema_view
from .drf_yasg_views import get_schema_view
from drf_yasg import openapi

# Conditionally include OAuth2 views, if OAuth2 is installed and configured for the API
try:
    import oauth2_provider.views as oauth2_views
except:
    pass

from . import views


schema_view = get_schema_view(
   openapi.Info(
      title='Mezzanine API',
      default_version='1.3.53',
      description='A REST Web API for the Mezzanine content management system with the Cartridge e-commerce extension.',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'sites', views.SiteViewSet)
router.register(r'redirects', views.RedirectViewSet)
router.register(r'settings', views.SettingViewSet)
router.register(r'pages', views.PageViewSet)
router.register(r'blogposts', views.BlogPostViewSet)
router.register(r'blogcategories', views.BlogCategoryViewSet)
router.register(r'galleries', views.GalleryViewSet)
router.register(r'galleryimages', views.GalleryImageViewSet)
router.register(r'threadedcomments', views.ThreadedCommentViewSet)
router.register(r'assignedkeywords', views.AssignedKeywordViewSet)
router.register(r'ratings', views.RatingViewSet)
router.register(r'systemsettings', views.SystemSettingViewSet)

# Conditionally include Cartridge viewsets, if the Cartridge package is installed
try:
  router.register(r'products', views.ProductViewSet)
  router.register(r'productimages', views.ProductImageViewSet)
  router.register(r'productoptions', views.ProductOptionViewSet)
  router.register(r'productvariations', views.ProductVariationViewSet)
  router.register(r'categories', views.CategoryViewSet)
  router.register(r'carts', views.CartViewSet)
  router.register(r'cartitems', views.CartItemViewSet)
  router.register(r'orders', views.OrderViewSet)
  router.register(r'orderitems', views.OrderItemViewSet)
  router.register(r'sales', views.SaleViewSet)
  router.register(r'discountcodes', views.DiscountCodeViewSet)
except:
    pass

urlpatterns = [
	url(r'^$', RedirectView.as_view(url='/api/docs', permanent=False)),
    url(r'^docs/(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^', include(router.urls)),
]

# Conditionally include OAuth2 views, if in installed_apps in settings
try:
    urlpatterns = [
        url(r'^auth/$', oauth2_views.AuthorizationView.as_view(), name="authorise"),
        url(r'^token/$', oauth2_views.TokenView.as_view(), name="token"),
        url(r'^revoke-token/$', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
    ] + urlpatterns
except:
    pass
