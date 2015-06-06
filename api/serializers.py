"""Serializers for the library app."""

from rest_framework import serializers

from models import MFASupport
from models import Organization

class MFASupportSerializer(serializers.ModelSerializer):

    """Serializer for the MFASupport."""

    class Meta:
        model = MFASupport

class OrganizationSerializer(serializers.ModelSerializer):

    """Serializer for the Organization."""

    class Meta:
        model = Organization
