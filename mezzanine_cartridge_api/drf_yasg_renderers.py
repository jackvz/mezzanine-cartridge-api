# Override the Swagger UI template
from drf_yasg.renderers import SwaggerUIRenderer

# SwaggerUIRenderer.template = 'swagger-ui.html'
class SwaggerUIRendererWithCorrectScheme(SwaggerUIRenderer):
    template = 'swagger-ui-http.html'
