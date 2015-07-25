# (c) 2014, Brian Coca <bcoca@ansible.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import

import math
import collections
from ansible import errors

def generate_fixed(a):
    return [1, 2, 3]

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

    return previous_dict + [new_element]

class FilterModule(object):
    ''' Ansible Antoine jinja2 filters '''

    def filters(self):
        return {
            'generate_fixed' : generate_fixed,
            'add_field_to_dict' : add_field_to_dict,
            'append' : append,

        }
