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

from onepanel.core.api.configuration import Configuration


class Transformer(object):
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
        'containers': 'list[Container]',
        'min_cpu': 'str',
        'min_memory': 'str',
        'max_cpu': 'str',
        'max_memory': 'str'
    }

    attribute_map = {
        'containers': 'containers',
        'min_cpu': 'minCpu',
        'min_memory': 'minMemory',
        'max_cpu': 'maxCpu',
        'max_memory': 'maxMemory'
    }

    def __init__(self, containers=None, min_cpu=None, min_memory=None, max_cpu=None, max_memory=None, local_vars_configuration=None):  # noqa: E501
        """Transformer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._containers = None
        self._min_cpu = None
        self._min_memory = None
        self._max_cpu = None
        self._max_memory = None
        self.discriminator = None

        if containers is not None:
            self.containers = containers
        if min_cpu is not None:
            self.min_cpu = min_cpu
        if min_memory is not None:
            self.min_memory = min_memory
        if max_cpu is not None:
            self.max_cpu = max_cpu
        if max_memory is not None:
            self.max_memory = max_memory

    @property
    def containers(self):
        """Gets the containers of this Transformer.  # noqa: E501


        :return: The containers of this Transformer.  # noqa: E501
        :rtype: list[Container]
        """
        return self._containers

    @containers.setter
    def containers(self, containers):
        """Sets the containers of this Transformer.


        :param containers: The containers of this Transformer.  # noqa: E501
        :type: list[Container]
        """

        self._containers = containers

    @property
    def min_cpu(self):
        """Gets the min_cpu of this Transformer.  # noqa: E501


        :return: The min_cpu of this Transformer.  # noqa: E501
        :rtype: str
        """
        return self._min_cpu

    @min_cpu.setter
    def min_cpu(self, min_cpu):
        """Sets the min_cpu of this Transformer.


        :param min_cpu: The min_cpu of this Transformer.  # noqa: E501
        :type: str
        """

        self._min_cpu = min_cpu

    @property
    def min_memory(self):
        """Gets the min_memory of this Transformer.  # noqa: E501


        :return: The min_memory of this Transformer.  # noqa: E501
        :rtype: str
        """
        return self._min_memory

    @min_memory.setter
    def min_memory(self, min_memory):
        """Sets the min_memory of this Transformer.


        :param min_memory: The min_memory of this Transformer.  # noqa: E501
        :type: str
        """

        self._min_memory = min_memory

    @property
    def max_cpu(self):
        """Gets the max_cpu of this Transformer.  # noqa: E501


        :return: The max_cpu of this Transformer.  # noqa: E501
        :rtype: str
        """
        return self._max_cpu

    @max_cpu.setter
    def max_cpu(self, max_cpu):
        """Sets the max_cpu of this Transformer.


        :param max_cpu: The max_cpu of this Transformer.  # noqa: E501
        :type: str
        """

        self._max_cpu = max_cpu

    @property
    def max_memory(self):
        """Gets the max_memory of this Transformer.  # noqa: E501


        :return: The max_memory of this Transformer.  # noqa: E501
        :rtype: str
        """
        return self._max_memory

    @max_memory.setter
    def max_memory(self, max_memory):
        """Sets the max_memory of this Transformer.


        :param max_memory: The max_memory of this Transformer.  # noqa: E501
        :type: str
        """

        self._max_memory = max_memory

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
        if not isinstance(other, Transformer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Transformer):
            return True

        return self.to_dict() != other.to_dict()
