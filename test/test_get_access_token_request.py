# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.20.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import onepanel.core.api
from onepanel.core.api.models.get_access_token_request import GetAccessTokenRequest  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestGetAccessTokenRequest(unittest.TestCase):
    """GetAccessTokenRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetAccessTokenRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.get_access_token_request.GetAccessTokenRequest()  # noqa: E501
        if include_optional :
            return GetAccessTokenRequest(
                username = '0', 
                token = '0'
            )
        else :
            return GetAccessTokenRequest(
        )

    def testGetAccessTokenRequest(self):
        """Test GetAccessTokenRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
