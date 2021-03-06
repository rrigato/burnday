from copy import deepcopy
from unittest.mock import patch

import unittest


class TestEntryBurnStatus(unittest.TestCase):


    def test_validate_location_burn_status(self):
        """Happy Path validate_location_burn_status returns a ValidRequest"""
        from burnday.entry.entry_burn_status import validate_location_burn_status
        mock_zip_code = 20002

        location_burn_status_request = validate_location_burn_status(zip_code=mock_zip_code)

        self.assertEqual(
            location_burn_status_request.request_filters["zip_code"], 
            mock_zip_code
        )



    def test_validate_location_burn_status_bad_input(self):
        """Unhappy Path validate_location_burn_status returns an InvalidRequest"""
        from burnday.entry.entry_burn_status import validate_location_burn_status
        from burnday.entry.request_objects import InvalidRequest
        mock_zip_code = 100000

        location_burn_status_request = validate_location_burn_status(zip_code=mock_zip_code)

        self.assertEqual(type(location_burn_status_request), InvalidRequest)



    @patch("burnday.entry.entry_burn_status.load_burn_status")
    def test_location_burn_status(self, mock_load_burn_status):
        """Happy Path ResponseSuccess returned with populated burn_status"""
        from burnday.entities.entity_model import BurnStatus
        from burnday.entry.entry_burn_status import location_burn_status
        from burnday.entry.request_objects import ValidRequest

        mock_zip_code = 20002
        mock_air_quality_index = 123
        burn_status_entity = BurnStatus()
        burn_status_entity.zip_code = mock_zip_code
        burn_status_entity.air_quality_index = mock_air_quality_index
        

        mock_load_burn_status.return_value = (burn_status_entity, None)

        zip_code_burn_status = location_burn_status(
            zip_code_request=ValidRequest(request_filters={"zip_code": mock_zip_code})
        )

        self.assertEqual(type(zip_code_burn_status.response_value.burn_status), str)


    @patch("burnday.entry.entry_burn_status.load_burn_status")
    def test_location_burn_status_unexpected_error(self, mock_load_burn_status):
        """ResponseFailure with error message on unexpected error"""
        from burnday.entry.entry_burn_status import location_burn_status
        from burnday.entry.request_objects import ValidRequest

        mock_error_message = "Network Error Connecting to external API"
        mock_zip_code = 99998
        mock_load_burn_status.return_value = (None, mock_error_message)


        zip_code_burn_status = location_burn_status(
            zip_code_request=ValidRequest(request_filters={"zip_code": mock_zip_code})
        )


        self.assertFalse(zip_code_burn_status)
        self.assertEqual(type(zip_code_burn_status.error_message), str)


    @patch("burnday.entry.entry_burn_status.load_burn_status")
    def test_location_burn_status_no_zip_match(self, mock_load_burn_status):
        """ResponseSuccess with response_value=None for no BurnStatus data for zip code"""
        from burnday.entry.entry_burn_status import location_burn_status
        from burnday.entry.request_objects import ValidRequest

        mock_zip_code = 99998

        mock_load_burn_status.return_value = (None, None)

        zip_code_burn_status = location_burn_status(
            zip_code_request=ValidRequest(request_filters={"zip_code": mock_zip_code})
        )

        self.assertIsNone(zip_code_burn_status.response_value)