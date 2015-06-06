from django.db import models

class Organization(models.Model):
    """ Model for Organization. """
    name = models.CharField(max_length=256)
    website = models.URLField()
    logo = models.URLField()
    twitter_handle = models.CharField(max_length=256)

class MFASupport(models.Model):
    """ Model for Multi-factor Authentication support."""
    documentation = models.URLField()
    organization = models.OneToOneField(Organization)
    sms = models.BooleanField(default=False)
    phone_call = models.BooleanField(default=False)
    email = models.BooleanField(default=False)
    hardware_token = models.BooleanField(default=False)
    software_implementation = models.BooleanField(default=False)
