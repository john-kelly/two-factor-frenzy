from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'organization', views.OrganizationViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls))
)
