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
from onepanel.core.api.api.service_service_api import ServiceServiceApi  # noqa: E501
from onepanel.core.api.rest import ApiException


class TestServiceServiceApi(unittest.TestCase):
    """ServiceServiceApi unit test stubs"""

    def setUp(self):
        self.api = onepanel.core.api.api.service_service_api.ServiceServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_service(self):
        """Test case for get_service

        """
        pass

    def test_list_services(self):
        """Test case for list_services

        """
        pass


if __name__ == '__main__':
    unittest.main()
