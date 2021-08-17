from django.urls import path, include
from rest_framework.routers import DefaultRouter

from values_principles.api.v1 import viewsets

router = DefaultRouter()

router.register("values", viewsets.ValueViewSet)
router.register("principles", viewsets.PrincipleViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
