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


class JobHistoryDefinitionProperties(Model):
    """JobHistoryDefinitionProperties

    :param datetime start_time: Gets the start time for this job.
    :param datetime end_time: Gets the end time for this job.
    :param datetime expected_execution_time: Gets the expected execution time
     for this job.
    :param str action_name: Gets the job history action name. Possible values
     include: 'MainAction', 'ErrorAction'
    :param str status: Gets the job history status. Possible values include:
     'Completed', 'Failed', 'Postponed'
    :param str message: Gets the message for the job history.
    :param int retry_count: Gets the retry count for job.
    :param int repeat_count: Gets the repeat count for the job.
    """ 

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'expected_execution_time': {'key': 'expectedExecutionTime', 'type': 'iso-8601'},
        'action_name': {'key': 'actionName', 'type': 'JobHistoryActionName'},
        'status': {'key': 'status', 'type': 'JobExecutionStatus'},
        'message': {'key': 'message', 'type': 'str'},
        'retry_count': {'key': 'retryCount', 'type': 'int'},
        'repeat_count': {'key': 'repeatCount', 'type': 'int'},
    }

    def __init__(self, start_time=None, end_time=None, expected_execution_time=None, action_name=None, status=None, message=None, retry_count=None, repeat_count=None, **kwargs):
        self.start_time = start_time
        self.end_time = end_time
        self.expected_execution_time = expected_execution_time
        self.action_name = action_name
        self.status = status
        self.message = message
        self.retry_count = retry_count
        self.repeat_count = repeat_count
