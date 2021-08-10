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
from onepanel.core.api.models.predictor import Predictor  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestPredictor(unittest.TestCase):
    """Predictor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Predictor
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.predictor.Predictor()  # noqa: E501
        if include_optional :
            return Predictor(
                node_selector = onepanel.core.api.models.node_selector.NodeSelector(
                    key = '0', 
                    value = '0', ), 
                server = onepanel.core.api.models.predictor_server.PredictorServer(
                    name = '0', 
                    runtime_version = '0', 
                    storage_uri = '0', 
                    limits = onepanel.core.api.models.resource_limits.ResourceLimits(
                        cpu = '0', 
                        memory = '0', ), )
            )
        else :
            return Predictor(
        )

    def testPredictor(self):
        """Test Predictor"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
