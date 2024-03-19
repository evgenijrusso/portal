"""
URL configuration for work project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the includes() function: from django.urls import includes, path
    2. Add a URL to urlpatterns:  path('blog/', includes('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers

from news.views.viewset import AuthorViewset, CategoryViewset, NewsViewset, ArticlesViewset, UserViewset


router = routers.DefaultRouter()
router.register(r'authors', AuthorViewset)
router.register(r'news', NewsViewset)
router.register(r'articles', ArticlesViewset, 'Articles')  # без добавление 'Articles' - ошибка с базовым роутером
router.register(r'categories', CategoryViewset)
router.register(r'user', UserViewset)


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('appointment.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('api/', include(router.urls)),
    # path('api-auth/', include('api.urls')),
]

admin.site.site_header = "Администрирование News Portal"
admin.site.site_title = "Админка"
admin.site.index_title = 'Новостной портал'