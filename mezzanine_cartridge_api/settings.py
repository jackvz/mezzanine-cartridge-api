# OAUTH2_PROVIDER = {
#     'SCOPES': {
#         'read': 'Read scope', 
#         'write': 'Write scope'
#     }
# }

CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK = {
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
}

SWAGGER_SETTINGS = {
    'LOGIN_URL': '/admin/login/',
    'LOGOUT_URL': '/admin/logout/',
    'DOC_EXPANSION': 'list',
    'USE_SESSION_AUTH': False,
    'APIS_SORTER': 'alpha',
    'SECURITY_DEFINITIONS': {

        # "basic": {
        #     "type": "basic"
        # },

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

        # "Password-based": {
        #     "type": "oauth2",
        #     "flow": "password",
        #     "tokenUrl": "/api/token/",
        #     "scopes": {
        #         "read": "Read scope", 
        #         "write": "Write scope"
        #     }
        # },

        # "Authorisation code": {
        #     "type": "oauth2",
        #     "flow": "accessCode",
        #     "authorizationUrl": "/api/auth/",
        #     "tokenUrl": "/api/token/",
        #     "scopes": {
        #         "read": "Read scope", 
        #         "write": "Write scope"
        #     }
        # }

    }
}

SWAGGER_SCHEME_HTTPS = False
