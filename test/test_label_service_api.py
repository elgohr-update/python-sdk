# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.15.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import onepanel.core.api
from onepanel.core.api.api.label_service_api import LabelServiceApi  # noqa: E501
from onepanel.core.api.rest import ApiException


class TestLabelServiceApi(unittest.TestCase):
    """LabelServiceApi unit test stubs"""

    def setUp(self):
        self.api = onepanel.core.api.api.label_service_api.LabelServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_labels(self):
        """Test case for add_labels

        """
        pass

    def test_delete_label(self):
        """Test case for delete_label

        """
        pass

    def test_get_available_labels(self):
        """Test case for get_available_labels

        """
        pass

    def test_get_labels(self):
        """Test case for get_labels

        """
        pass

    def test_replace_labels(self):
        """Test case for replace_labels

        """
        pass


if __name__ == '__main__':
    unittest.main()
