#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# Authors:
# @author: David Blaisonneau <david.blaisonneau@orange.com>
# @author: Arnaud Morin <arnaud1.morin@orange.com>

from foreman.itemSmartClassParameter\
    import ItemSmartClassParameter


class SubItemSmartClassParameter(ItemSmartClassParameter):
    """
    ItemOverrideValues class
    Represent the content of a foreman smart class parameter as a dict
    """
    setInParentPayload = False
    objNameSet = 'smart_class_parameters'

    def __init__(self, api, key, parentName, parentPayloadObject,
                 parentKey, *args, **kwargs):
        """ Function __init__
        Represent the content of a foreman object as a dict

        @param api: The foreman api
        @param key: The object Key
        @param parentName: The object parent name (eg: smart_class_parameters)
        @param parentPayloadObject: The object parent
                                    payload object (eg: smart_class_parameter)
        @param parentKey: The object parent key
        @param *args, **kwargs: the dict representation
        @return RETURN: Itself
        """
        self.parentKey = parentKey
        ItemSmartClassParameter.__init__(self, api, key, parentName,
                                         parentPayloadObject,
                                         *args, **kwargs)
