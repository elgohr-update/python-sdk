# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import onepanel.core.api
from onepanel.core.api.models.model_condition import ModelCondition  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestModelCondition(unittest.TestCase):
    """ModelCondition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ModelCondition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.model_condition.ModelCondition()  # noqa: E501
        if include_optional :
            return ModelCondition(
                last_transition_time = '0', 
                status = '0', 
                type = '0'
            )
        else :
            return ModelCondition(
        )

    def testModelCondition(self):
        """Test ModelCondition"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
