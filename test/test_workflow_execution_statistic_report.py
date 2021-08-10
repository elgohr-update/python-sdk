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
from onepanel.core.api.models.workflow_execution_statistic_report import WorkflowExecutionStatisticReport  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestWorkflowExecutionStatisticReport(unittest.TestCase):
    """WorkflowExecutionStatisticReport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WorkflowExecutionStatisticReport
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.workflow_execution_statistic_report.WorkflowExecutionStatisticReport()  # noqa: E501
        if include_optional :
            return WorkflowExecutionStatisticReport(
                total = 56, 
                last_executed = '0', 
                running = 56, 
                completed = 56, 
                failed = 56, 
                terminated = 56
            )
        else :
            return WorkflowExecutionStatisticReport(
        )

    def testWorkflowExecutionStatisticReport(self):
        """Test WorkflowExecutionStatisticReport"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
