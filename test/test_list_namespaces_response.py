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
from onepanel.core.api.models.list_namespaces_response import ListNamespacesResponse  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestListNamespacesResponse(unittest.TestCase):
    """ListNamespacesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListNamespacesResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.list_namespaces_response.ListNamespacesResponse()  # noqa: E501
        if include_optional :
            return ListNamespacesResponse(
                count = 56, 
                namespaces = [
                    onepanel.core.api.models.namespace.Namespace(
                        name = '0', )
                    ], 
                page = 56, 
                pages = 56, 
                total_count = 56
            )
        else :
            return ListNamespacesResponse(
        )

    def testListNamespacesResponse(self):
        """Test ListNamespacesResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
