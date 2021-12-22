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
        mock_air_quality_index = 79
        mock_fine_particulate_matter_2_5 = 24.4
        mock_coarse_particulate_matter_10 = 111


        burn_status_entity = BurnStatus()


        burn_status_entity.burn_day = date.fromisoformat(mock_burn_day)
        burn_status_entity.burn_status = mock_burn_status
        burn_status_entity.county_name = mock_county_name
        burn_status_entity.air_quality_index = mock_air_quality_index
        burn_status_entity.fine_particulate_matter_2_5 = mock_fine_particulate_matter_2_5
        burn_status_entity.coarse_particulate_matter_10 = mock_coarse_particulate_matter_10
        

        self.assertEqual(burn_status_entity.burn_day.isoformat(), mock_burn_day)
        self.assertEqual(burn_status_entity.burn_status, mock_burn_status)
        self.assertEqual(burn_status_entity.county_name, mock_county_name)
        self.assertEqual(burn_status_entity.air_quality_index, mock_air_quality_index)
        self.assertEqual(
            burn_status_entity.fine_particulate_matter_2_5, 
            mock_fine_particulate_matter_2_5
        )
        self.assertEqual(
            burn_status_entity.coarse_particulate_matter_10, 
            mock_coarse_particulate_matter_10
        )



    def test_burn_status_bad_input_str_attributes(self):
        """BurnStatus str attributes passed invalid input raises TypeError"""
        from burnday.entities.entity_model import BurnStatus

        mock_invalid_types = [
            set(["a", "b"]),
            3005,
            11.29,
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


    def test_burn_status_bad_input_numeric_attributes(self):
        """BurnStatus numeric attributes passed invalid input raises TypeError"""
        from burnday.entities.entity_model import BurnStatus

        mock_invalid_types = [
            set(["a", "b"]),
            "3005",
            "11.29",
            (1, 2, 3),
            {},
            ["a", "list"]
        ]

        for mock_invalid_type in mock_invalid_types:
            with self.subTest(mock_invalid_type=mock_invalid_type):

                mock_burn_status = BurnStatus()
                
                with self.assertRaises(TypeError):
                    mock_burn_status.air_quality_index = mock_invalid_type

                with self.assertRaises(TypeError):
                    mock_burn_status.fine_particulate_matter_2_5 = mock_invalid_type

                with self.assertRaises(TypeError):
                    mock_burn_status.coarse_particulate_matter_10 = mock_invalid_type