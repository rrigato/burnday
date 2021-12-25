import unittest

class TestZipCodeBurnEvaluationLogic(unittest.TestCase):

    def test_default_burn_rules(self):
        """Default ruleset for burning"""
        from burnday.entities.entity_model import BurnStatus
        from burnday.usecase.zip_code_burn_evaluation_logic import default_burn_rules

        aqi_test_values = [
            {"aqi_input": 17, "zip_code": 20002, "expected_burn_status": "air quality status is in the healthy range"},
            {"aqi_input": 74, "zip_code": 20002, "expected_burn_status": "air quality status is in the moderate range"},
            {"aqi_input": 123, "zip_code": 20002, "expected_burn_status": "air quality status is in the unhealthy for sensitive groups range"},
            {"aqi_input": 189, "zip_code": 20002, "expected_burn_status": "air quality status is in the unhealthy range"},
            {"aqi_input": 201, "zip_code": 20002, "expected_burn_status": "air quality status is in the very unhealthy range"},
            {"aqi_input": 349, "zip_code": 20002, "expected_burn_status": "air quality status is in the hazardous range"}
        ]

        for aqi_test_value in aqi_test_values:
            with self.subTest(aqi_test_value=aqi_test_value):
                burn_status_entity = BurnStatus()
                burn_status_entity.air_quality_index = aqi_test_value["aqi_input"]
                burn_status_entity.air_quality_index = aqi_test_value["aqi_input"]
                
                default_burn_rules(populated_burn_status=burn_status_entity)

                self.assertEqual(
                    burn_status_entity.burn_status, 
                    aqi_test_value["expected_burn_status"]
                )


    def test_california_valley_burn_rules(self):
        """California valley zip code based ruleset"""
        pass

