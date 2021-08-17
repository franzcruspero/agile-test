from rest_framework import serializers

from values_principles.models import Value, Principle


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ["id", "name", "description"]


class PrincipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Principle
        fields = ["id", "name", "description"]
