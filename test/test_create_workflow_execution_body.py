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
from onepanel.core.api.models.create_workflow_execution_body import CreateWorkflowExecutionBody  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestCreateWorkflowExecutionBody(unittest.TestCase):
    """CreateWorkflowExecutionBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateWorkflowExecutionBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.create_workflow_execution_body.CreateWorkflowExecutionBody()  # noqa: E501
        if include_optional :
            return CreateWorkflowExecutionBody(
                workflow_template_uid = '0', 
                workflow_template_version = '0', 
                parameters = [
                    onepanel.core.api.models.parameter.Parameter(
                        name = '0', 
                        value = '0', 
                        type = '0', 
                        display_name = '0', 
                        hint = '0', 
                        required = True, 
                        visibility = '0', 
                        options = [
                            onepanel.core.api.models.parameter_option.ParameterOption(
                                name = '0', 
                                value = '0', )
                            ], )
                    ], 
                labels = [
                    onepanel.core.api.models.key_value.KeyValue(
                        key = '0', 
                        value = '0', )
                    ]
            )
        else :
            return CreateWorkflowExecutionBody(
        )

    def testCreateWorkflowExecutionBody(self):
        """Test CreateWorkflowExecutionBody"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
