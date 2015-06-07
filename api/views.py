from django.http import HttpResponse

from rest_framework import filters
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from serializers import OrganizationSerializer
from models import Organization


class OrganizationViewSet(viewsets.ReadOnlyModelViewSet):

    """Readonly Organization endpoint."""

    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('website')

    @list_route()
    def top_3_of_category(self, request):
        """ Top 3 Organization of Category API Endpoint."""

        query_params = self.request.query_params

        top_3 = Organization.top_3_of_category(query_params.get('category', ''))

        org_serializer = self.get_serializer(top_3, many=True)

        return Response(org_serializer.data)
