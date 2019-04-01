# Override the Swagger UI template
from drf_yasg.renderers import SwaggerUIRenderer

class SwaggerUIRendererWithAllSchemes(SwaggerUIRenderer):
    template = 'swagger-ui-all-schemes.html'
