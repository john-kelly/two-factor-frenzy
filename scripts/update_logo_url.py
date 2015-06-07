"""Script to convert yaml info to json.

Usage
-----

./manage.py runscript update_logo_url

"""


from api.models import *


def run():
    """Entry point for script."""

    orgs = Organization.objects.all()

    for org in orgs:
        # correct the site logo
        logo = org.logo
        new_logo_base = 'https://twofactorauth.org/img/' + org.category + '/'
        fixed_logo = logo.replace('https://twofactorauth.org/img/', new_logo_base)
        org.logo = fixed_logo
        org.save()
