name = 'mezzanine_cartridge_api'

from custom_settings.loader import load_settings
load_settings(__name__)

# Override the Swagger UI template
from mezzanine.conf import settings
from rest_framework_swagger import renderers

renderers.SwaggerUIRenderer.template = 'rest_framework_swagger/http.html'
if settings.SWAGGER_SCHEME_HTTPS:
    renderers.SwaggerUIRenderer.template = 'rest_framework_swagger/https.html'
