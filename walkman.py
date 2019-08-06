# -*- coding: utf-8 -*-
###
# (C) Copyright (2012-2017) Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###

from pprint import pprint
from hpOneView.oneview_client import OneViewClient
from hpOneView.exceptions import HPOneViewException
#from config_loader import try_load_from_file
import json

TEMP_DIR=/root/Walkman/scratch/

# You can use username/password or sessionID for authentication.
# Be sure to inform a valid and active sessionID.
config = {
    "ip": "<oneview_ip>",
    "credentials": {
        "userName": "<username>",
        "password": "<password>",
        "sessionID": "<sessionID>"
    }
}


# Try load config from a file (if there is a config file)
# The below line loads config.json file if present in current directory
fin = open('config.json', 'r')
#config = try_load_from_file(fin)
config = json.load(fin)

oneview_client = OneViewClient(config)


# Get all enclosures
try:
    print("Get all enclosures")
    enclosures = oneview_client.enclosures.get_all()
    for enc in enclosures:
        print('  {name}'.format(**enc))

###################################################################

    # Get all, with default
    print("Get all Enclosure Groups")
    egs = oneview_client.enclosure_groups.get_all()
#    pprint(egs)
    for eg in egs:
        print('  {name}'.format(**eg))

###################################################################
    # Get all logical enclosures
    print("Get all logical enclosures")
    logical_enclosures = oneview_client.logical_enclosures.get_all()
    for enc in logical_enclosures:
        #print('   %s' % enc['name'])
        print('   %s' % enc['enclosureGroupUri'])
    enclosureGroupURI = enc['enclosureGroupUri']
###################################################################

    # Get all
    print("\nGet list of all server profile templates")
    all_templates = oneview_client.server_profile_templates.get_by('enclosureGroupUri', enclosureGroupURI)
    for template in all_templates:
        print('  %s' % template['name'])
        print('  %s' % template['uri'])
        print('  %s' % template['serverHardwareTypeUri'])
        serverHardwareTypeUri = template['serverHardwareTypeUri']
###################################################################
    # Get Server Hardware which matches specified server hardware type and
    # has no server profile assigned to it

    
    # Get list of all server hardware resources
    print("Get list of all server hardware resources")
    server_hardware_all = oneview_client.server_hardware.get_by('serverGroupUri', enclosureGroupURI)
    for serv in server_hardware_all:
        if serv['serverHardwareTypeUri'] == serverHardwareTypeUri:
            if serv['serverProfileUri'] == None:
                print('  %s' % serv['name'])
                print('  %s' % serv['state'])
                print('  %s' % serv['uri'])

#    print(serv)

###################################################################


except HPOneViewException as e:
    print(e.msg)

