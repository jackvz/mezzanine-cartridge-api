from django.conf.urls import include, url
from django.views.generic.base import RedirectView

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

# Conditionally include OAuth2 views, if in installed_apps in settings
try:
    import oauth2_provider.views as oauth2_views
except RuntimeError:
    pass

from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'sites', views.SiteViewSet)
router.register(r'redirects', views.RedirectViewSet)
router.register(r'settings', views.SettingViewSet)
router.register(r'page', views.PageViewSet)
router.register(r'blogpost', views.BlogPostViewSet)
router.register(r'blogcategory', views.BlogCategoryViewSet)
router.register(r'gallery', views.GalleryViewSet)
router.register(r'galleryimage', views.GalleryImageViewSet)
router.register(r'threadedcomment', views.ThreadedCommentViewSet)
router.register(r'assignedkeyword', views.AssignedKeywordViewSet)
router.register(r'rating', views.RatingViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'productimage', views.ProductImageViewSet)
router.register(r'productoption', views.ProductOptionViewSet)
router.register(r'productvariation', views.ProductVariationViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'orderitem', views.OrderItemViewSet)
router.register(r'sale', views.SaleViewSet)
router.register(r'discountcode', views.DiscountCodeViewSet)

urlpatterns = [
	url(r'^$', RedirectView.as_view(url='/api/docs', permanent=False)),
	url(r'^docs', get_swagger_view(title='Mezzanine API')),
    url(r'^', include(router.urls)),
]

# Conditionally include OAuth2 views, if in installed_apps in settings
try:
    urlpatterns = [
        url(r'^auth/$', oauth2_views.AuthorizationView.as_view(), name="authorise"),
        url(r'^token/$', oauth2_views.TokenView.as_view(), name="token"),
        url(r'^revoke-token/$', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
    ] + urlpatterns
except NameError:
    pass
