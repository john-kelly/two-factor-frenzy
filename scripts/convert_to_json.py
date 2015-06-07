"""Script to convert yaml info to json.

Usage
-----

./manage.py runscript convert_to_json

"""

import os
import yaml
from api.models import *

def run():
    """Entry point for script."""

    # get each file in the directory
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

                # now populate the db
                for org in list_objects:
                    # get the MFA status for each organization
                    try:
                        doc = org['doc']
                    except:
                        doc = ''
                    try:
                        sms = org['sms']
                    except:
                        sms = ''
                    try:
                        phone = org['phone']
                    except:
                        phone = ''
                    try:
                        email = org['email']
                    except:
                        email = ''
                    try:
                        hardware = org['hardware']
                    except:
                        hardware = ''
                    try:
                        software = org['software']
                    except:
                        software = ''

                    mfa = MFASupport(
                        documentation=doc, sms=sms,
                        phone_call=phone, email=email,
                        hardware_token=hardware,
                        software_implementation=software
                    )
                    mfa.save()

                    # create each organization and apply its MFA status
                    try:
                        name = org['name']
                    except:
                        name = ''

                    try:
                        url = org['url']
                    except:
                        url = ''

                    try:
                        img = 'https://twofactorauth.org/img' + tag + org['img']
                    except:
                        img = 'https://twofactorauth.org/img/logo.png'

                    try:
                        twitter = org['twitter']
                    except:
                        twitter = ''

                    organization = Organization(
                        name=name, category=tag,
                        website=url, logo=img,
                        twitter_handle=twitter, mfa_support=mfa
                    )
                    organization.save()
