# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.20.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from onepanel.core.api.configuration import Configuration


class WorkflowExecutionStatisticReport(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'total': 'int',
        'last_executed': 'str',
        'running': 'int',
        'completed': 'int',
        'failed': 'int',
        'terminated': 'int'
    }

    attribute_map = {
        'total': 'total',
        'last_executed': 'lastExecuted',
        'running': 'running',
        'completed': 'completed',
        'failed': 'failed',
        'terminated': 'terminated'
    }

    def __init__(self, total=None, last_executed=None, running=None, completed=None, failed=None, terminated=None, local_vars_configuration=None):  # noqa: E501
        """WorkflowExecutionStatisticReport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total = None
        self._last_executed = None
        self._running = None
        self._completed = None
        self._failed = None
        self._terminated = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if last_executed is not None:
            self.last_executed = last_executed
        if running is not None:
            self.running = running
        if completed is not None:
            self.completed = completed
        if failed is not None:
            self.failed = failed
        if terminated is not None:
            self.terminated = terminated

    @property
    def total(self):
        """Gets the total of this WorkflowExecutionStatisticReport.  # noqa: E501


        :return: The total of this WorkflowExecutionStatisticReport.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this WorkflowExecutionStatisticReport.


        :param total: The total of this WorkflowExecutionStatisticReport.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def last_executed(self):
        """Gets the last_executed of this WorkflowExecutionStatisticReport.  # noqa: E501


        :return: The last_executed of this WorkflowExecutionStatisticReport.  # noqa: E501
        :rtype: str
        """
        return self._last_executed

    @last_executed.setter
    def last_executed(self, last_executed):
        """Sets the last_executed of this WorkflowExecutionStatisticReport.


        :param last_executed: The last_executed of this WorkflowExecutionStatisticReport.  # noqa: E501
        :type: str
        """

        self._last_executed = last_executed

    @property
    def running(self):
        """Gets the running of this WorkflowExecutionStatisticReport.  # noqa: E501


        :return: The running of this WorkflowExecutionStatisticReport.  # noqa: E501
        :rtype: int
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this WorkflowExecutionStatisticReport.


        :param running: The running of this WorkflowExecutionStatisticReport.  # noqa: E501
        :type: int
        """

        self._running = running

    @property
    def completed(self):
        """Gets the completed of this WorkflowExecutionStatisticReport.  # noqa: E501


        :return: The completed of this WorkflowExecutionStatisticReport.  # noqa: E501
        :rtype: int
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this WorkflowExecutionStatisticReport.


        :param completed: The completed of this WorkflowExecutionStatisticReport.  # noqa: E501
        :type: int
        """

        self._completed = completed

    @property
    def failed(self):
        """Gets the failed of this WorkflowExecutionStatisticReport.  # noqa: E501


        :return: The failed of this WorkflowExecutionStatisticReport.  # noqa: E501
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this WorkflowExecutionStatisticReport.


        :param failed: The failed of this WorkflowExecutionStatisticReport.  # noqa: E501
        :type: int
        """

        self._failed = failed

    @property
    def terminated(self):
        """Gets the terminated of this WorkflowExecutionStatisticReport.  # noqa: E501


        :return: The terminated of this WorkflowExecutionStatisticReport.  # noqa: E501
        :rtype: int
        """
        return self._terminated

    @terminated.setter
    def terminated(self, terminated):
        """Sets the terminated of this WorkflowExecutionStatisticReport.


        :param terminated: The terminated of this WorkflowExecutionStatisticReport.  # noqa: E501
        :type: int
        """

        self._terminated = terminated

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkflowExecutionStatisticReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowExecutionStatisticReport):
            return True

        return self.to_dict() != other.to_dict()
