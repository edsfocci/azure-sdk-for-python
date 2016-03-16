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


class VirtualNetworkGatewaySku(Model):
    """
    VirtualNetworkGatewaySku details

    :param str name: Gateway sku name -Basic/HighPerformance/Standard.
     Possible values include: 'Basic', 'HighPerformance', 'Standard'
    :param str tier: Gateway sku tier -Basic/HighPerformance/Standard.
     Possible values include: 'Basic', 'HighPerformance', 'Standard'
    :param int capacity: The capacity
    """ 

    _attribute_map = {
        'name': {'key': 'name', 'type': 'VirtualNetworkGatewaySkuName'},
        'tier': {'key': 'tier', 'type': 'VirtualNetworkGatewaySkuTier'},
        'capacity': {'key': 'capacity', 'type': 'int'},
    }

    def __init__(self, name=None, tier=None, capacity=None, **kwargs):
        self.name = name
        self.tier = tier
        self.capacity = capacity