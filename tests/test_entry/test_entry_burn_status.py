from copy import deepcopy
import unittest

class TestEntryBurnStatus(unittest.TestCase):


    def test_validate_county_burn_status(self):
        """Happy Path validate_county_burn_status returns a ValidRequest"""
        from burnday.entry.entry_burn_status import validate_county_burn_status
        mock_county_name = "Sequoia National Park and Forest"

        county_burn_status_request = validate_county_burn_status(county_name=mock_county_name)

        self.assertEqual(
            county_burn_status_request.request_filters["county_name"], 
            mock_county_name
        )


    
    def test_validate_county_burn_status_bad_input(self):
        """Unhappy Path validate_county_burn_status returns a ValidRequest"""
        from burnday.entry.entry_burn_status import validate_county_burn_status
        from burnday.entry.request_objects import InvalidRequest
        mock_county_name = ["Sequoia National Park and Forest", "Fresno"]

        county_burn_status_request = validate_county_burn_status(county_name=mock_county_name)

        self.assertEqual(type(county_burn_status_request), InvalidRequest)
