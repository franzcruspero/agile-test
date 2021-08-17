from rest_framework import serializers, viewsets

from values_principles.api.v1.serializers import ValueSerializer, PrincipleSerializer
from values_principles.models import Value, Principle


class ValueViewSet(viewsets.ModelViewSet):
    serializer_class = ValueSerializer
    queryset = Value.objects.all()


class PrincipleViewSet(viewsets.ModelViewSet):
    serializer_class = PrincipleSerializer
    queryset = Principle.objects.all()
