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

from msrest.serialization import Model


class ValidateCustomDomainOutput(Model):
    """
    Output of custom domain validation

    :param bool custom_domain_validated: Indicates whether the custom domain
     is validated or not
    :param str reason: The reason why the custom domain is not valid
    :param str message: The message on why the custom domain is not valid
    """ 

    _attribute_map = {
        'custom_domain_validated': {'key': 'customDomainValidated', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, custom_domain_validated=None, reason=None, message=None, **kwargs):
        self.custom_domain_validated = custom_domain_validated
        self.reason = reason
        self.message = message
