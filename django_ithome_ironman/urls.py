"""django_ithome_ironman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt # New library
from django.views.generic import TemplateView
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token
)
from graphene_django.views import GraphQLView
from news import views
from treemenu.views import TreeView, TreePDFView


urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += [
    # API base url
    path("api/news/", include("news.urls")),
    path("api/example/", views.ExampleView.as_view()),

    # drf-jwt
    path('api/token-auth/', obtain_jwt_token),
    path('api/token-refresh/', refresh_jwt_token),
    path('api/token-verify/', verify_jwt_token),

    # graphene-django
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),

    # treeview
    path('tree/', TreeView.as_view()),
    path('tree.pdf/', TreePDFView.as_view()),

    path('', TemplateView.as_view(template_name='home.html')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns