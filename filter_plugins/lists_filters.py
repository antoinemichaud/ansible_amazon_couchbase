from __future__ import absolute_import

import math
import collections
from ansible import errors

def add_field_to_dict(previous_dict, new_fields):
    print previous_dict
    print new_fields
    if previous_dict is None:
        return new_fields
    for k, v in new_fields.iteritems():
        previous_dict[k] = v
    return previous_dict

def append(previous_list, new_element):
    print previous_list
    print previous_list
    if previous_list is None:
        return [new_element]

    return previous_list + [new_element]

class FilterModule(object):
    ''' Ansible Antoine jinja2 filters '''

    def filters(self):
        return {
            'add_field_to_dict' : add_field_to_dict,
            'append' : append,

        }
