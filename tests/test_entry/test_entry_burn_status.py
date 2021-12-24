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


    @patch("burnday.entry.entry_burn_status.burn_status_for_zip")
    def test_location_burn_status_no_zip_match(self, mock_burn_status_for_zip):
        """ResponseSuccess with response_value=None for no BurnStatus data for zip code"""
        from burnday.entry.entry_burn_status import location_burn_status
        from burnday.entry.request_objects import ValidRequest

        mock_zip_code = 99998

        zip_code_burn_status = location_burn_status(
            zip_code_request=ValidRequest(request_filters={"zip_code": mock_zip_code})
        )

        self.assertIsNone(zip_code_burn_status.response_value)