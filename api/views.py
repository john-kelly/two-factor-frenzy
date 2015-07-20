from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from rest_framework import filters
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from serializers import OrganizationSerializer
from models import Organization
from models import SiteRequest

import json


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


def site_requests(request):
    """View the page after submitting a new site.

    A new site can be submitted from the form here or from the extension.

    Returns HttpResponse

    """

    site_requests = SiteRequest.objects.all().order_by(
        '-status', '-num_requests'
    )

    return render(request, "site_requests.html", {
        'site_requests': site_requests
    })


@csrf_exempt
def add_site(request):
    """Handle incoming POST requests to add new sites to the list.

    Creates a new SiteRequest object for sites submitted via the extension.

    Returns JSON response back to the extension.

    """

    add_site = request.POST.get('site', '')

    if not add_site:
        data = {
             'status': 'fail'
         }
    else:
        # ensure that the URL is valid
        validate = URLValidator()
        try:
            validate(add_site)
        except ValidationError, e:
            print "\nError adding site: %s" % add_site
            print e

        # if a request already exists for this site, get it.
        # otherwise, create a new site request.
        request, created = SiteRequest.objects.get_or_create(website=add_site)
        request.num_requests += 1
        request.save()

        data = {
            'status': 'ok',
            'site': add_site,
        }

    return HttpResponse(json.dumps(data), content_type = "application/json")
