from copy import deepcopy
from unittest.mock import patch

import json
import unittest

class TestPersistantStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mock_project_secrets = {
            "mock_key1": "mock_secret0",
            "mock_key2": "mock_secret1",
            "mock_key3": "mock_secret2"
        }
        cls.MOCK_AWS_REGION = "us-east-1"

    @patch("os.environ.get")
    @patch("boto3.client")
    def test_get_burnday_secrets(self, mock_boto3_client, mock_os_environ_get):
        """Happy Path, api secrets and config returned"""
        from burnday.repo.persistant_storage import get_burnday_secrets

        mock_boto3_client.return_value.get_parameter.return_value = deepcopy(
            {
                "Parameter":{
                    "Value": json.dumps(deepcopy(self.mock_project_secrets))
                }
            }
        )
        mock_os_environ_get.return_value = self.MOCK_AWS_REGION


        burnday_project_config, config_retrieval_error = get_burnday_secrets()


        mock_boto3_client.assert_called_once_with("ssm", region_name="us-east-1")
        self.assertIsNone(config_retrieval_error)

    def test_get_burnday_secrets_unexpected_error(self):
        """Unhappy Path, unable to load api keys on unexpected error"""
        pass
