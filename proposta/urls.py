# -*- Mode: Python; coding: utf-8 -*-
from django.conf.urls import *
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf import settings
from . import views

admin.site.site_header = 'Brasil Geradores'            # default: "Django Administration"
admin.site.index_title = 'ADMINISTRAÇÃO'               # default: "Site administration"
admin.site.site_title = 'BRG'                          # default: "Django site admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.matriz, name='matriz'),
    path('proxima-pagina/', views.proxima_pagina, name='proxima_pagina'),
    path('contato/', views.contato, name='contato'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
