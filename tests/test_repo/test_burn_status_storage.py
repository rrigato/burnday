from copy import deepcopy
from unittest.mock import patch

import json
import unittest

class TestBurnStatusStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mock_project_secrets = {
            "mock_key1": "mock_secret0",
            "mock_key2": "mock_secret1",
            "mock_key3": "mock_secret2"
        }
        cls.MOCK_AWS_REGION = "us-east-1"


    @patch("burnday.repo.burn_status_storage.get_burnday_secrets")
    def test_load_burn_status(self, mock_get_burnday_secrets):
        """Happy Path BurnStatus Entity returned from API"""
        from burnday.repo.burn_status_storage import load_burn_status

        mock_zip_code = 20002
        mock_air_quality_index = 123
        mock_get_burnday_secrets.return_value = (deepcopy(self.mock_project_secrets), None)

        burn_status_entity, load_burn_status_error = load_burn_status(zip_code=mock_zip_code)

        '''
            TODO - 
            Remove test of outgoing secrets arguements
            patch of outgoing API call
            that returns the API response json structure then tests the burn_status_entity 
            returned is as expected
        '''
        mock_get_burnday_secrets.assert_called_once_with()

        self.assertIsNotNone(burn_status_entity.burn_day)
        # self.assertEqual(burn_status_entity.air_quality_index, mock_air_quality_index)
        # self.assertEqual(burn_status_entity.zip_code, mock_zip_code)
        # self.assertIsNone(load_burn_status_error)

        


