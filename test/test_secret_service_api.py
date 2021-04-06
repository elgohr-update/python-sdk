# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.20.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import onepanel.core.api
from onepanel.core.api.api.secret_service_api import SecretServiceApi  # noqa: E501
from onepanel.core.api.rest import ApiException


class TestSecretServiceApi(unittest.TestCase):
    """SecretServiceApi unit test stubs"""

    def setUp(self):
        self.api = onepanel.core.api.api.secret_service_api.SecretServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_secret_key_value(self):
        """Test case for add_secret_key_value

        """
        pass

    def test_create_secret(self):
        """Test case for create_secret

        """
        pass

    def test_delete_secret(self):
        """Test case for delete_secret

        """
        pass

    def test_delete_secret_key(self):
        """Test case for delete_secret_key

        """
        pass

    def test_get_secret(self):
        """Test case for get_secret

        """
        pass

    def test_list_secrets(self):
        """Test case for list_secrets

        """
        pass

    def test_secret_exists(self):
        """Test case for secret_exists

        """
        pass

    def test_update_secret_key_value(self):
        """Test case for update_secret_key_value

        """
        pass


if __name__ == '__main__':
    unittest.main()
