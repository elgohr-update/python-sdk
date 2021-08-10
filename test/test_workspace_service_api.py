# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import onepanel.core.api
from onepanel.core.api.api.workspace_service_api import WorkspaceServiceApi  # noqa: E501
from onepanel.core.api.rest import ApiException


class TestWorkspaceServiceApi(unittest.TestCase):
    """WorkspaceServiceApi unit test stubs"""

    def setUp(self):
        self.api = onepanel.core.api.api.workspace_service_api.WorkspaceServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_workspace(self):
        """Test case for create_workspace

        """
        pass

    def test_delete_workspace(self):
        """Test case for delete_workspace

        """
        pass

    def test_get_workspace(self):
        """Test case for get_workspace

        """
        pass

    def test_get_workspace_container_logs(self):
        """Test case for get_workspace_container_logs

        """
        pass

    def test_get_workspace_statistics_for_namespace(self):
        """Test case for get_workspace_statistics_for_namespace

        """
        pass

    def test_list_workspaces(self):
        """Test case for list_workspaces

        """
        pass

    def test_list_workspaces_field(self):
        """Test case for list_workspaces_field

        """
        pass

    def test_pause_workspace(self):
        """Test case for pause_workspace

        """
        pass

    def test_resume_workspace(self):
        """Test case for resume_workspace

        """
        pass

    def test_retry_last_workspace_action(self):
        """Test case for retry_last_workspace_action

        """
        pass

    def test_update_workspace(self):
        """Test case for update_workspace

        """
        pass

    def test_update_workspace_status(self):
        """Test case for update_workspace_status

        """
        pass


if __name__ == '__main__':
    unittest.main()
