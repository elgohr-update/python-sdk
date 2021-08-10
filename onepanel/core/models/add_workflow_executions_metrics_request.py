# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from onepanel.core.configuration import Configuration


class AddWorkflowExecutionsMetricsRequest(object):
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
        'namespace': 'str',
        'uid': 'str',
        'override': 'bool',
        'metrics': 'list[Metric]'
    }

    attribute_map = {
        'namespace': 'namespace',
        'uid': 'uid',
        'override': 'override',
        'metrics': 'metrics'
    }

    def __init__(self, namespace=None, uid=None, override=None, metrics=None, local_vars_configuration=None):  # noqa: E501
        """AddWorkflowExecutionsMetricsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._namespace = None
        self._uid = None
        self._override = None
        self._metrics = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if uid is not None:
            self.uid = uid
        if override is not None:
            self.override = override
        if metrics is not None:
            self.metrics = metrics

    @property
    def namespace(self):
        """Gets the namespace of this AddWorkflowExecutionsMetricsRequest.  # noqa: E501


        :return: The namespace of this AddWorkflowExecutionsMetricsRequest.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this AddWorkflowExecutionsMetricsRequest.


        :param namespace: The namespace of this AddWorkflowExecutionsMetricsRequest.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def uid(self):
        """Gets the uid of this AddWorkflowExecutionsMetricsRequest.  # noqa: E501


        :return: The uid of this AddWorkflowExecutionsMetricsRequest.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this AddWorkflowExecutionsMetricsRequest.


        :param uid: The uid of this AddWorkflowExecutionsMetricsRequest.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def override(self):
        """Gets the override of this AddWorkflowExecutionsMetricsRequest.  # noqa: E501


        :return: The override of this AddWorkflowExecutionsMetricsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._override

    @override.setter
    def override(self, override):
        """Sets the override of this AddWorkflowExecutionsMetricsRequest.


        :param override: The override of this AddWorkflowExecutionsMetricsRequest.  # noqa: E501
        :type: bool
        """

        self._override = override

    @property
    def metrics(self):
        """Gets the metrics of this AddWorkflowExecutionsMetricsRequest.  # noqa: E501


        :return: The metrics of this AddWorkflowExecutionsMetricsRequest.  # noqa: E501
        :rtype: list[Metric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this AddWorkflowExecutionsMetricsRequest.


        :param metrics: The metrics of this AddWorkflowExecutionsMetricsRequest.  # noqa: E501
        :type: list[Metric]
        """

        self._metrics = metrics

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
        if not isinstance(other, AddWorkflowExecutionsMetricsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddWorkflowExecutionsMetricsRequest):
            return True

        return self.to_dict() != other.to_dict()
