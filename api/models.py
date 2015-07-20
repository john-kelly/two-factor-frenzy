from django.db import models


class MFASupport(models.Model):
    """ Model for Multi-factor Authentication support."""
    documentation = models.URLField(blank=True, null=True)
    sms = models.BooleanField(default=False)
    phone_call = models.BooleanField(default=False)
    email = models.BooleanField(default=False)
    hardware_token = models.BooleanField(default=False)
    software_implementation = models.BooleanField(default=False)

class EncryptionSupport(models.Model):
    """ Model for various encrytpion methods support."""
    sha_status = models.BooleanField(default=False)

class Organization(models.Model):
    """ Model for Organization. """
    name = models.CharField(max_length=256)
    category = models.CharField(max_length=256, default='')
    website = models.URLField(blank=True, null=True)
    logo = models.URLField(blank=True, null=True)
    twitter_handle = models.CharField(max_length=256, default='')
    mfa_support = models.OneToOneField(MFASupport, null=True, blank=True)
    encryption_support = models.OneToOneField(
        EncryptionSupport, null=True, blank=True
    )

    # TODO
    def calculate_safety(self):
        return 1

    # TODO generalize this.
    @staticmethod
    def top_3_of_category(category):
        """ Returns top 5 safest Organizations based on their calculated safety

        Returns list because can not filter by model method."""

        orgs_of_category = Organization.objects.filter(category=category)

        return sorted(
            orgs_of_category, key=lambda org:org.calculate_safety()
        )[-3:]

class SiteRequest(models.Model):
    """ Model for requests that users make to add new sites to the database."""

    # status of the site request
    RECEIVED = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    REJECTED = -1

    STATUS_CHOICES = (
        (RECEIVED, 'Received'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
        (REJECTED, 'Rejected')
    )

    website = models.URLField(unique=True)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=RECEIVED)
    notes = models.CharField(max_length=256, default='')
    num_requests = models.IntegerField(default=0)

    def status_verbose(self):
        """ Return readable text for the given field. """
        return dict(SiteRequest.STATUS_CHOICES)[self.status]
