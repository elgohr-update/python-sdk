# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.15.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import onepanel.core.api
from onepanel.core.api.models.get_labels_response import GetLabelsResponse  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestGetLabelsResponse(unittest.TestCase):
    """GetLabelsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetLabelsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.get_labels_response.GetLabelsResponse()  # noqa: E501
        if include_optional :
            return GetLabelsResponse(
                labels = [
                    onepanel.core.api.models.key_value.KeyValue(
                        key = '0', 
                        value = '0', )
                    ]
            )
        else :
            return GetLabelsResponse(
        )

    def testGetLabelsResponse(self):
        """Test GetLabelsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
