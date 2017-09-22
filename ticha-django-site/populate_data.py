#!/usr/local/lib/python-virtualenv/ticha-django/bin/python3
"""This script parses JSON data exported from Omeka saves it into the HandwrittenText models in the
   database. Some of the data from the JSON file does not go into the database, but is instead saved
   in a configuration file for a TimelineJS app.

   The JSON data comes from ticha.haverford.edu/documents/api/items

   The reason this script doesn't simply pull the data from the website itself is that the Omeka API
   sends different data depending on whether it is Python or Firefox (or any other web browser) that
   is requesting the data. I do not know why this happens.
"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ticha.settings')

import django
django.setup()

import json
import re
import argparse

from handwritten_texts.models import HandwrittenText


def do_everything(fpath, debug=False):
    """Do all the things. If debug is True, then the script will run but no
       changes will be made to any files or databases.
    """
    try:
        with open(fpath, 'r') as response:
            metadata = json.loads(response.read())
    except IOError:
        print('Error: unable to read from {}'.format(fpath))
    else:
        populate_database(metadata, debug=debug)
        generate_timeline_config(metadata, debug=debug)


def populate_database(metadata, debug=False):
    """Populate the database from the Omeka metadata. If debug is True, then 
       the script will run but no changes will be made to the database.
    """
    print('Found %d documents' % len(metadata))
    # iterate over each document in the metadata
    for i, doc_dict in enumerate(extract_documents(metadata)):
        # make sure the document has a title attribute
        if 'title' not in doc_dict:
            doc_dict['title'] = ''
        # add the document to the database
        try:
            add_handwritten(doc_dict, debug=debug)
            if not debug:
                print('Added', end= ' ')
            else:
                print('Would have added', end=' ')
            print('document {} ({})'.format(i + 1, doc_dict['title']))
        except django.db.utils.DataError as e:
            print('Database error, could not add document {} ({})'.format(i + 1, doc_dict['title']))
            print(e)

#TIMELINE_CONFIG_PATH = '/var/www/html/json/timeline2.json'
TIMELINE_CONFIG_PATH = 'handwritten_texts/static/handwritten_texts/json/timeline2.json'
def generate_timeline_config(metadata, debug=False):
    """Generate the timeline config file from the Omeka metadata. If debug is 
       True, then the script will run but no changes will be made to the config
       file.
    """
    timeline_slides = []
    # iterate over each document in the metadata
    for i, doc_dict in enumerate(extract_documents(metadata)):
        # add the timeline information to the list
        slide_obj = create_slide_object(doc_dict)
        if slide_obj:
            timeline_slides.append(slide_obj)
    timeline_obj = {'events':timeline_slides}
    if not debug:
        try:
            with open(TIMELINE_CONFIG_PATH, 'w') as fsock:
                json.dump(timeline_obj, fsock, ensure_ascii=False)
        except IOError:
            print('Error: could not write to %s' % TIMELINE_CONFIG_PATH)

def add_handwritten(doc_dict, debug=False):
    """Create an instance of a HandwrittenText model in the database with the
       given attributes.
    """
    doc = HandwrittenText.objects.get_or_create(title=doc_dict['title'])[0]
    for key, val in doc_dict.items():
        if key == 'identifier': key = 'slug'
        if hasattr(doc, key):
            # format dates correctly
            if key == 'date_digitized':
                m,d,y = re.search(r'([0-9]+)/([0-9]+)/([0-9]+)', val).groups()
                if len(y) == 2:
                    y = '20' + y
                val = y + '-' + m + '-' + d
            elif key == 'permission_file':
                val = fix_permission_file(val)
            setattr(doc, key, val)
    if not debug:
        doc.save()

def fix_permission_file(val):
    """Change the permission file from a HTML anchor tag to a bare URL."""
    href_index = val.find('href="')
    if href_index != -1:
        url_start = href_index + len('href="')
        url_end = val.find('"', url_start)
        url = val[url_start:url_end]
        url = url.replace('https', 'http', 1)
        return url
    else:
        return val

def create_slide_object(doc_dict):
    """Given a dict of attributes from Omeka, create a JSON slide object in the
       format expected by TimelineJS

       See: https://timeline.knightlab.com/docs/json-format.html#json-slide
    """
    slide_obj = {}
    if 'tl_text' in doc_dict and 'tl_headline' in doc_dict \
       and 'tl_media_thumbnail' in doc_dict and 'tl_start_date' in doc_dict:
        slide_obj['text'] = {'text':doc_dict['tl_text'],
                             'headline':doc_dict['tl_headline']}
        slide_obj['media'] = {'url':get_media_url(doc_dict)}
        # parse the start date
        date_str = doc_dict['tl_start_date']
        split_date = [int(x) for x in date_str.split('/')]
        if len(split_date) == 3:
            month, day, year = split_date
        elif len(split_date) == 3:
            month, year = split_date
            day = 1
        else:
            # default value since field is required
            month, day, year = 1, 1, 1700
        slide_obj['start_date'] = {'year':year, 'month':month, 'day':day}
    return slide_obj

def get_media_url(doc_dict):
    """Get the correct URL for the timeline images."""
    try:
        first_page = doc_dict['page'].split('-', maxsplit=1)[0]
        fp = doc_dict['identifier'] + '_' + first_page + '.jpg'
        return '../../images/jpg/' + fp
    except KeyError:
        return doc_dict['tl_media_thumbnail']

def extract_documents(metadata):
    """Given a metadata object in the format returned by the Omeka API, 
       generate a sequence of dicts where each dict represents the key-value 
       pairs of a single document. Since the response is an iterate, you'll
       have to call list(extract_documents) to get it as a list.

       This is the only method in the module that has to carry about the format
       of Omeka's JSON response.
    """
    for doc in metadata:
        document_dict = {'omeka_id':doc.get('id', '')}
        # iterate over the objects containing the key-value pairs
        # potentially skipping the loop if the doc has no 'element_texts' key
        for j in doc.get('element_texts', []):
            key = omeka_to_django_key(j['element']['name'])
            val = omeka_to_django_value(j['text'])
            document_dict[key] = val
        yield document_dict

def omeka_to_django_key(key):
    """Change a string from its name in Omeka (e.g., 'Primary Parties') to its
       name in the Django model (e.g., 'primary_parties').
    """
    key = key.lower().replace(' ', '_').replace('(', '').replace(')', '')
    key = key.replace('/', '_')
    return key

def omeka_to_django_value(val):
    """Same as omeka_to_django_key, except for the database values."""
    return val.replace('<span>', '').replace('</span>', '')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('fpath', help='File containing Omeka export')
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()
    do_everything(args.fpath, debug=args.debug)
