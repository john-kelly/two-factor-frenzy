from django.http import HttpResponse
from django.shortcuts import render

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
    search_fields = ('website',)

    @list_route()
    def top_3(self, request):
        """ Top 3 Organization of filter API Endpoint."""

        # Currently only can get top 3 of category.

        query_params = self.request.query_params

        category = query_params.get('category', '')

        # TODO Return Top3 of all categories
        if not category:
            # Return empty response
            return Response([])

        top_3 = Organization.top_3_of_category(category)

        org_serializer = self.get_serializer(top_3, many=True)

        return Response(org_serializer.data)


def index(request):
    """View the index page.

    Returns HttpResponse

    """

    return render(request, "index.html")


def added(request):
    """View the page after submitting a new site.

    A new site can be submitted from the form here or from the extension.

    Returns HttpResponse

    """

    add_site = 'example.com/your-website'

    return render(request, "added.html", {
        'add_site': add_site
    })
