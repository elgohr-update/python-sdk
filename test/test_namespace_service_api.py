# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.20.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import onepanel.core.api
from onepanel.core.api.api.namespace_service_api import NamespaceServiceApi  # noqa: E501
from onepanel.core.api.rest import ApiException


class TestNamespaceServiceApi(unittest.TestCase):
    """NamespaceServiceApi unit test stubs"""

    def setUp(self):
        self.api = onepanel.core.api.api.namespace_service_api.NamespaceServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_namespace(self):
        """Test case for create_namespace

        """
        pass

    def test_list_namespaces(self):
        """Test case for list_namespaces

        """
        pass


if __name__ == '__main__':
    unittest.main()
