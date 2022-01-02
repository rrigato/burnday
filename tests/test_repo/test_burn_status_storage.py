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
        """Happy Path BurnStatus Entity created from API response"""
        from burnday.repo.burn_status_storage import load_burn_status
        from datetime import date
        from urllib.parse import urlparse

        mock_zip_code = 20002
        mock_get_burnday_secrets.return_value = (deepcopy(self.mock_project_secrets), None)

        mock_urlopen.return_value.__enter__.return_value.getcode.return_value = 200
        mock_urlopen.return_value.__enter__.return_value.read.return_value = json.dumps(
            deepcopy(self.one_airnow_api_forecast)
        ).encode("utf-8")



        burn_status_entity, load_burn_status_error = load_burn_status(zip_code=mock_zip_code)


        
        args, kwargs = mock_urlopen.call_args

        self.assertEqual(len(args), 1)
        self.assertEqual(len(kwargs), 0)
        outgoing_api_call = urlparse(args[0].get_full_url())

        self.assertEqual(outgoing_api_call.hostname, "www.airnowapi.org")
        self.assertEqual(outgoing_api_call.scheme, "https")
        self.assertEqual(outgoing_api_call.path, "/aq/forecast/zipCode")
        self.assertEqual(
            outgoing_api_call.query, 
            "api_key=1234&distance=500&format=json&zipCode=20002"
        )

        self.assertEqual(
            burn_status_entity.burn_day, 
            date.fromisoformat(self.one_airnow_api_forecast[0]["DateForecast"].strip())
        )
        self.assertEqual(
            burn_status_entity.air_quality_index, 
            self.one_airnow_api_forecast[0]["AQI"]
        )
        self.assertEqual(burn_status_entity.zip_code, mock_zip_code)
        self.assertIsNone(load_burn_status_error)

 
    @patch("burnday.repo.burn_status_storage.urlopen")
    @patch("burnday.repo.burn_status_storage.get_burnday_secrets")
    def test_load_burn_status_multiple_forecasts(self, mock_get_burnday_secrets, mock_urlopen):
        """Oldest DateForecast selected from api response with multiple forecast dicts"""
        from burnday.repo.burn_status_storage import load_burn_status
        from datetime import date

        mock_zip_code = 20002
        mock_get_burnday_secrets.return_value = (deepcopy(self.mock_project_secrets), None)

        mock_urlopen.return_value.__enter__.return_value.getcode.return_value = 200
        multiple_forecasts = deepcopy(self.multiple_airnow_api_forecasts)[1:]
        
        multiple_forecasts.append(deepcopy(self.multiple_airnow_api_forecasts)[0])
        mock_urlopen.return_value.__enter__.return_value.read.return_value = json.dumps(
            multiple_forecasts
        ).encode("utf-8")



        burn_status_entity, load_burn_status_error = load_burn_status(zip_code=mock_zip_code)


        self.assertEqual(
            burn_status_entity.burn_day, 
            date.fromisoformat(self.multiple_airnow_api_forecasts[0]["DateForecast"].strip())
        )
        self.assertEqual(
            burn_status_entity.air_quality_index, 
            self.multiple_airnow_api_forecasts[0]["AQI"]
        )
        self.assertEqual(burn_status_entity.zip_code, mock_zip_code)
        self.assertIsNone(load_burn_status_error)


    @patch("burnday.repo.burn_status_storage.urlopen")
    @patch("burnday.repo.burn_status_storage.get_burnday_secrets")
    def test_load_burn_status_http_400_status_code(self, mock_get_burnday_secrets, mock_urlopen):
        """Unhappy Path api returns http 400"""
        from burnday.repo.burn_status_storage import load_burn_status

        mock_zip_code = 20002
        mock_get_burnday_secrets.return_value = (deepcopy(self.mock_project_secrets), None)

        mock_urlopen.return_value.__enter__.return_value.getcode.return_value = 400

        burn_status_entity, load_burn_status_error = load_burn_status(zip_code=mock_zip_code)


        self.assertEqual(mock_urlopen.return_value.__enter__.return_value.read.call_count, 0)


    @unittest.skip("TODO - body of test case")
    @patch("burnday.repo.burn_status_storage.urlopen")
    @patch("burnday.repo.burn_status_storage.get_burnday_secrets")
    def test_load_burn_status_empty_list(self, mock_get_burnday_secrets, mock_urlopen):
        """Api returns [] in post body"""
        from burnday.repo.burn_status_storage import load_burn_status
        from datetime import date

        mock_zip_code = 20002
        mock_get_burnday_secrets.return_value = (deepcopy(self.mock_project_secrets), None)

        mock_urlopen.return_value.__enter__.return_value.read.return_value = json.dumps(
            []
        ).encode("utf-8")



        burn_status_entity, load_burn_status_error = load_burn_status(zip_code=mock_zip_code)


        '''
            TODO - what to say when unable to retrieve burn status for a location,
            currently says
            <speak>Something went wrong when attempting to retrieve the burn status for that location, please try again later</speak>
            set in externals.alexa_intents.burn_status_intent
        '''