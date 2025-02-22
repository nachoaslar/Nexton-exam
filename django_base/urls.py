from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework.routers import DefaultRouter

from django.contrib import admin
from django.urls import path, include, re_path
from candidates.urls import router as candidates_router


schema_view = get_schema_view(
    openapi.Info(
        title="Base project API",
        default_version="v1",
        description="Base project documentation",
        contact=openapi.Contact(email="contact@linkchar.com"),
    ),
    public=True,
)

base_router = DefaultRouter()
base_router.registry.extend(candidates_router.registry)

# fmt: off
#<-------------- Django + libraries urls -------------->
urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
]

# <-------------- Swagger urls -------------->
urlpatterns += [
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

#<-------------- Our apps includes -------------->
urlpatterns += [
]

#<-------------- Our base router -------------->
urlpatterns += [path("api/", include(base_router.urls)),]

# fmt: on
