from django.db import models

class MFASupport(models.Model):
    """ Model for Multi-factor Authentication support."""
    documentation = models.URLField(blank=True, null=True)
    sms = models.BooleanField(default=False)
    phone_call = models.BooleanField(default=False)
    email = models.BooleanField(default=False)
    hardware_token = models.BooleanField(default=False)
    software_implementation = models.BooleanField(default=False)

class Organization(models.Model):
    """ Model for Organization. """
    name = models.CharField(max_length=256)
    category = models.CharField(max_length=256, default='')
    website = models.URLField(blank=True, null=True)
    logo = models.URLField(blank=True, null=True)
    twitter_handle = models.CharField(max_length=256, default='')
    mfa_support = models.OneToOneField(MFASupport, null=True, blank=True)
