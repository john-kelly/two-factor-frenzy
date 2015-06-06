from django.http import HttpResponse

from rest_framework import viewsets

from serializers import OrganizationSerializer
from models import Organization


class OrganizationViewSet(viewsets.ReadOnlyModelViewSet):

    """Readonly Organization endpoint."""

    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
