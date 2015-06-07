"""Serializers for the library app."""

from rest_framework import serializers

from models import EncryptionSupport
from models import MFASupport
from models import Organization

class MFASupportSerializer(serializers.ModelSerializer):

    """Serializer for the MFASupport."""

    class Meta:
        model = MFASupport

class EncryptionSupportSerializer(serializers.ModelSerializer):

    """Serializer for the EncryptionSupport."""

    class Meta:
        model = EncryptionSupport

class OrganizationSerializer(serializers.ModelSerializer):

    """Serializer for the Organization."""

    mfa_support = MFASupportSerializer()
    encryption_support = EncryptionSupportSerializer()

    class Meta:
        model = Organization
