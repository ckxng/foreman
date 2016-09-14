===========
Foreman
===========

* Python library to manipulate The Foreman through the API
* Authors:
    - David Blaisonneau david.blaisonneau@orange.com
    - Arnaud Morin arnaud1.morin@orange.com
* License: Apache 2.0


Usage
-----------

Load the code::
    >>> from foreman import Foreman
    >>> foreman = Foreman(login=args["admin"], password=args["password"],
     ip=args["ip"], ca_cert=args['example.crt'])

Manipulate hosts::
    >>> foreman.hosts.keys()
    dict_keys(['foreman.my.domain', 'server1.my.domain', 'server2.my.domain'])
    >>> foreman.hosts['foreman.my.domain']
    {'compute_resource_name': None, 'certname': 'foreman.my.domain', ...
    >>> foreman.hosts['foreman.my.domain']['operatingsystem_name']
    'Ubuntu 14.04.2 LTS'

List of managed objects
-----------------------

- domains
- smartProxies
- puppetClasses
- operatingSystems
- architectures
- subnets
- hostgroups
- hosts
- computeResources
- environments
- configTemplates
- smartClassParameters
- settings
- ptables
- media

Debug the API calls
--------------------
Explore the api foreman.api object, and the 'history' list, containing the
last api calls
