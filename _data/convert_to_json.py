"""Script to convert yaml info to json.

Usage
-----

./manage.py runscript

"""

import os
import yaml

def run():
    """Entry point for script."""

    # get each file in the directory
    for fn in os.listdir('.'):
        # if it is a yaml file
        if fn.endswith('.yml'):
            # get the filename to serve as the organization tag
            filename = os.path.splitext(fn)
            tag = filename[0]
            print tag
            # open the file for processing
            with open(fn, 'r') as content_file:
                # load the yaml into the generator, create a list of objects
                content = content_file.read()
                generator = yaml.load_all(content)
                list_content = list(generator)
                index = list_content[0].keys()[0]
                list_objects = list_content[0][index]

                # now write to the model
                for website in list_objects:
                    # print website

run()


# convert that website yaml to json
    # pass the filename as a tag
    # take non-existent fields into account: if not present, set to False
