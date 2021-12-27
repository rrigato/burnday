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
        mock_boto3_client.return_value.get_parameter.assert_called_once_with(
            Name="/burnday/v1", WithDecryption=True
        )
        self.assertEqual(burnday_project_config, self.mock_project_secrets)
        self.assertIsNone(config_retrieval_error)


    @patch("os.environ.get")
    @patch("boto3.client")
    def test_get_burnday_secrets_unexpected_error(self, mock_boto3_client, mock_os_environ_get):
        """Unhappy Path, unable to load config due to unexpected SDK error"""
        from burnday.repo.persistant_storage import get_burnday_secrets

        mock_error_message = (
            "An error occurred (ParameterNotFound) when calling the GetParameter operation"
        )
        mock_boto3_client.return_value.get_parameter.side_effect = RuntimeError(mock_error_message)
        mock_os_environ_get.return_value = self.MOCK_AWS_REGION


        burnday_project_config, config_retrieval_error = get_burnday_secrets()

        
        self.assertIsNone(burnday_project_config)
        self.assertEqual(type(config_retrieval_error), str)