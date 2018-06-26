"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

urlpatterns = [
    url(r'^$', views.index_redirect, name='index_redirect'),
    url(r'^7ninja$', views.index_redirect, name='index_redirect'),
    # url(r'^$', include('crud.urls')),
    # url(r'^crud/', include('crud.urls')),
    url(r'^7ninja/', include('crud.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('web.api')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^obtain-auth-token/$', obtain_auth_token),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]
