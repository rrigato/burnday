from copy import deepcopy
from unittest.mock import patch

import json
import unittest

class TestBurnStatusStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mock_project_secrets = {
            "airnow_key": 1234,
            "mock_key2": "mock_secret1",
            "mock_key3": "mock_secret2"
        }
        cls.MOCK_AWS_REGION = "us-east-1"

        with open("tests/events/airnow_api/multiple_forecasts.json", "r") as api_request:
            cls.multiple_airnow_api_forecasts = json.load(api_request)

        with open("tests/events/airnow_api/one_forecast.json", "r") as api_request:
            cls.one_airnow_api_forecast = json.load(api_request)


    @patch("burnday.repo.burn_status_storage.urlopen")
    @patch("burnday.repo.burn_status_storage.get_burnday_secrets")
    def test_load_burn_status(self, mock_get_burnday_secrets, mock_urlopen):
        """Happy Path BurnStatus Entity returned from API"""
        from burnday.repo.burn_status_storage import load_burn_status
        from urllib.parse import urlparse

        mock_zip_code = 20002
        mock_air_quality_index = 123
        mock_get_burnday_secrets.return_value = (deepcopy(self.mock_project_secrets), None)

        mock_urlopen.return_value.__enter__.return_value.getcode.return_value = 200
        mock_urlopen.return_value.__enter__.return_value.read.return_value = json.dumps(
            deepcopy(self.multiple_airnow_api_forecasts)
        ).encode("utf-8")


        burn_status_entity, load_burn_status_error = load_burn_status(zip_code=mock_zip_code)

        
        args, kwargs = mock_urlopen.return_value.__enter__.return_value

        self.assertEqual(len(args), 1)
        self.assertEqual(len(kwargs), 0)
        outgoing_api_call = urlparse(args[0].get_full_url())

        '''
            TODO - 
            Remove test of outgoing secrets arguements
            patch of outgoing API call
            that returns the API response json structure then tests the burn_status_entity 
            returned is as expected
        '''

        self.assertIsNotNone(burn_status_entity.burn_day)
        # self.assertEqual(burn_status_entity.air_quality_index, mock_air_quality_index)
        # self.assertEqual(burn_status_entity.zip_code, mock_zip_code)
        # self.assertIsNone(load_burn_status_error)

        


    @patch("burnday.repo.burn_status_storage.urlopen")
    @patch("burnday.repo.burn_status_storage.get_burnday_secrets")
    def test_load_burn_status_http_400_status_code(self, mock_get_burnday_secrets, mock_urlopen):
        """Unhappy Path api returns http 400"""
        from burnday.repo.burn_status_storage import load_burn_status

        mock_zip_code = 20002
        mock_air_quality_index = 123
        mock_get_burnday_secrets.return_value = (deepcopy(self.mock_project_secrets), None)

        mock_urlopen.return_value.__enter__.return_value.getcode.return_value = 400

        burn_status_entity, load_burn_status_error = load_burn_status(zip_code=mock_zip_code)


        self.assertEqual(mock_urlopen.return_value.__enter__.return_value.read.call_count, 0)
