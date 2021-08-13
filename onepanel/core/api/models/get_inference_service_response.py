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


class GetInferenceServiceResponse(object):
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
        'ready': 'bool',
        'conditions': 'list[InferenceServiceCondition]',
        'predict_url': 'str'
    }

    attribute_map = {
        'ready': 'ready',
        'conditions': 'conditions',
        'predict_url': 'predictUrl'
    }

    def __init__(self, ready=None, conditions=None, predict_url=None, local_vars_configuration=None):  # noqa: E501
        """GetInferenceServiceResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ready = None
        self._conditions = None
        self._predict_url = None
        self.discriminator = None

        if ready is not None:
            self.ready = ready
        if conditions is not None:
            self.conditions = conditions
        if predict_url is not None:
            self.predict_url = predict_url

    @property
    def ready(self):
        """Gets the ready of this GetInferenceServiceResponse.  # noqa: E501


        :return: The ready of this GetInferenceServiceResponse.  # noqa: E501
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """Sets the ready of this GetInferenceServiceResponse.


        :param ready: The ready of this GetInferenceServiceResponse.  # noqa: E501
        :type: bool
        """

        self._ready = ready

    @property
    def conditions(self):
        """Gets the conditions of this GetInferenceServiceResponse.  # noqa: E501


        :return: The conditions of this GetInferenceServiceResponse.  # noqa: E501
        :rtype: list[InferenceServiceCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this GetInferenceServiceResponse.


        :param conditions: The conditions of this GetInferenceServiceResponse.  # noqa: E501
        :type: list[InferenceServiceCondition]
        """

        self._conditions = conditions

    @property
    def predict_url(self):
        """Gets the predict_url of this GetInferenceServiceResponse.  # noqa: E501


        :return: The predict_url of this GetInferenceServiceResponse.  # noqa: E501
        :rtype: str
        """
        return self._predict_url

    @predict_url.setter
    def predict_url(self, predict_url):
        """Sets the predict_url of this GetInferenceServiceResponse.


        :param predict_url: The predict_url of this GetInferenceServiceResponse.  # noqa: E501
        :type: str
        """

        self._predict_url = predict_url

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
        if not isinstance(other, GetInferenceServiceResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetInferenceServiceResponse):
            return True

        return self.to_dict() != other.to_dict()