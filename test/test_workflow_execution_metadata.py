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
from onepanel.core.api.models.workflow_execution_metadata import WorkflowExecutionMetadata  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestWorkflowExecutionMetadata(unittest.TestCase):
    """WorkflowExecutionMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WorkflowExecutionMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.workflow_execution_metadata.WorkflowExecutionMetadata()  # noqa: E501
        if include_optional :
            return WorkflowExecutionMetadata(
                url = '0'
            )
        else :
            return WorkflowExecutionMetadata(
        )

    def testWorkflowExecutionMetadata(self):
        """Test WorkflowExecutionMetadata"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
