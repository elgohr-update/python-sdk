# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.17.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from onepanel.core.api.configuration import Configuration


class IsValidTokenResponse(object):
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
        'domain': 'str',
        'token': 'str',
        'username': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'token': 'token',
        'username': 'username'
    }

    def __init__(self, domain=None, token=None, username=None, local_vars_configuration=None):  # noqa: E501
        """IsValidTokenResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._domain = None
        self._token = None
        self._username = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if token is not None:
            self.token = token
        if username is not None:
            self.username = username

    @property
    def domain(self):
        """Gets the domain of this IsValidTokenResponse.  # noqa: E501


        :return: The domain of this IsValidTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this IsValidTokenResponse.


        :param domain: The domain of this IsValidTokenResponse.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def token(self):
        """Gets the token of this IsValidTokenResponse.  # noqa: E501


        :return: The token of this IsValidTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this IsValidTokenResponse.


        :param token: The token of this IsValidTokenResponse.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def username(self):
        """Gets the username of this IsValidTokenResponse.  # noqa: E501


        :return: The username of this IsValidTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this IsValidTokenResponse.


        :param username: The username of this IsValidTokenResponse.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if not isinstance(other, IsValidTokenResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IsValidTokenResponse):
            return True

        return self.to_dict() != other.to_dict()
