# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class RestoreResponse(Resource):
    """
    Response for a restore site request

    :param str id: Resource Id
    :param str name: Resource Name
    :param str location: Resource Location
    :param str type: Resource type
    :param dict tags: Resource tags
    :param str operation_id: When server starts the restore process, it will
     return an OperationId identifying that particular restore operation
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'operation_id': {'key': 'properties.operationId', 'type': 'str'},
    }

    def __init__(self, location, id=None, name=None, type=None, tags=None, operation_id=None, **kwargs):
        super(RestoreResponse, self).__init__(id=id, name=name, location=location, type=type, tags=tags, **kwargs)
        self.operation_id = operation_id
