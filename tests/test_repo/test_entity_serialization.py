from copy import deepcopy

import json
import unittest

class TestEntitySerialization(unittest.TestCase):

    def test_create_burn_status(self):
        """Happy Path entity created"""
        from burnday.entities.entity_model import BurnStatus
        from burnday.repo.entity_serialization import create_burn_status
        from datetime import date

        mock_burn_day = date.fromisoformat("3005-11-29")
        mock_burn_status = "No Burning Unless Registered"
        mock_zip_code = 20002


        burn_status_entity, entity_creation_error = create_burn_status(
            burn_day=mock_burn_day,
            burn_status=mock_burn_status,
            zip_code=mock_zip_code
        )


        self.assertIsInstance(burn_status_entity, BurnStatus)
        self.assertIsNone(entity_creation_error)


    def test_create_burn_status_invalid_input(self):
        """Unhappy Path entity passed a str instead of datetime.date for entity creation"""
        from burnday.repo.entity_serialization import create_burn_status

        mock_burn_day = "3005-11-29"
        mock_burn_status = "No Burning Unless Registered"
        mock_zip_code = 20002


        burn_status_entity, entity_creation_error = create_burn_status(
            burn_day=mock_burn_day,
            burn_status=mock_burn_status,
            zip_code=mock_zip_code
        )


        self.assertEqual(type(entity_creation_error), str)
        self.assertIsNone(burn_status_entity)
