from copy import deepcopy
import unittest

class TestEntityModel(unittest.TestCase):
    def test_burn_status(self):
        """BurnStatus entity created"""
        from burnday.entities.entity_model import BurnStatus
        from datetime import date

        mock_burn_day = "3005-11-29"
        mock_burn_status = "Burning Discouraged"
        mock_county_name = "Mock County"


        burn_status_entity = BurnStatus()


        burn_status_entity.burn_day = date.fromisoformat(mock_burn_day)
        burn_status_entity.burn_status = mock_burn_status
        burn_status_entity.county_name = mock_county_name

        self.assertEqual(burn_status_entity.burn_day.isoformat(), mock_burn_day)
        self.assertEqual(burn_status_entity.burn_status, mock_burn_status)
        self.assertEqual(burn_status_entity.county_name, mock_county_name)



    def test_burn_status_bad_input(self):
        """BurnStatus entity passed invalid input raises TypeError"""
        from burnday.entities.entity_model import BurnStatus

        mock_invalid_types = [
            set(["a", "b"]),
            1, 
            2.0,
            (1, 2, 3),
            {},
            ["a", "list"]
        ]

        for mock_invalid_type in mock_invalid_types:
            with self.subTest(mock_invalid_type=mock_invalid_type):

                mock_burn_status = BurnStatus()
                
                with self.assertRaises(TypeError):
                    mock_burn_status.burn_day = mock_invalid_type

                with self.assertRaises(TypeError):
                    mock_burn_status.burn_status = mock_invalid_type

                with self.assertRaises(TypeError):
                    mock_burn_status.county_name = mock_invalid_type