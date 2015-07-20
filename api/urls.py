from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'organization', views.OrganizationViewSet)

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^add_site/', views.add_site, name='add_site'),
    url(r'^site_requests/', views.site_requests, name='added'),
    url(r'^api/', include(router.urls))
)
