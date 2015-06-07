"""Script to convert yaml info to json.

Usage
-----

./manage.py runscript update_logo_url

"""

import os
import yaml
from api.models import *


def run():
    """Entry point for script."""

    for fn in os.listdir('_data/'):
        # if it is a yaml file
        if fn.endswith('.yml') and fn != "main.yml" and fn != "providers.yml":
            # get the filename to serve as the organization tag
            filename = os.path.splitext(fn)
            tag = filename[0]
            print tag
            # open the file for processing
            with open('_data/' + fn, 'r') as content_file:
                # load the yaml into the generator, create a list of objects
                content = content_file.read()
                generator = yaml.load_all(content)
                list_content = list(generator)
                index = list_content[0].keys()[0]
                list_objects = list_content[0][index]

                for org in list_objects:
                    website = org['url']
                    try:
                        img = 'https://twofactorauth.org/img/' + tag + '/' + org['img']
                    except:
                        img = 'https://twofactorauth.org/img/logo.png'
                    print
                    print org['name']
                    print org['url']
                    organization = Organization.objects.get(website=website)
                    organization.logo = img
                    organization.save()
