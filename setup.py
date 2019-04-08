import setuptools

with open('readme.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'mezzanine_cartridge_api',
    version = '1.3.8',
    author = 'Jack van Zyl',
    author_email = 'jackvanzyl@icloud.com',
    description = 'A REST Web API for Mezzanine CMS with the Cartridge e-commerce extension',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/jackvz/mezzanine-cartridge-api',
    packages = setuptools.find_packages(),
    data_files=[('readme', ['readme.md']), 
        ('templates', ['mezzanine_cartridge_api/templates/swagger-ui-all-schemes.html']),
        ('static', [
            'mezzanine_cartridge_api/static/swagger-ui-bundle-http.js',
            'mezzanine_cartridge_api/static/swagger-ui-bundle-https.js',
            'mezzanine_cartridge_api/static/swagger-ui-standalone-preset.js',
        ])
    ],
    include_package_data=True,
    install_requires=[
        'django-custom-settings==0.1.4',
        'django-oauth-toolkit==1.1.1',
        'django-cors-middleware==1.3.1',
        'djangorestframework==3.9.2',
        'djangorestframework-api-key==0.3.1',
        'drf_yasg==1.15.0'
    ],
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)