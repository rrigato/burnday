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


    def test_california_valley_default_burn_rules(self):
        """California valley default burn ruleset"""
        from burnday.entities.entity_model import BurnStatus
        from burnday.usecase.zip_code_burn_evaluation_logic import california_valley_default_burn_rules


        pm_2_5_values = [
            {"pm_2_5_input": 0.5, "expected_burn_status": "burning discouraged"},
            {"pm_2_5_input": 17.0, "expected_burn_status": "burning discouraged"},
            {"pm_2_5_input": 20.1, "expected_burn_status": "no burning unless registered"},
            {"pm_2_5_input": 64.4, "expected_burn_status": "no burning unless registered"},
            {"pm_2_5_input": 65.2, "expected_burn_status": "no burning for all"},
            {"pm_2_5_input": 79.7, "expected_burn_status": "no burning for all"}
        ]

        for pm_2_5_value in pm_2_5_values:
            with self.subTest(pm_2_5_value=pm_2_5_value):
                burn_status_entity = BurnStatus()
                burn_status_entity.fine_particulate_matter_2_5 = pm_2_5_value["pm_2_5_input"]
                
                california_valley_default_burn_rules(populated_burn_status=burn_status_entity)

                self.assertEqual(
                    burn_status_entity.burn_status, 
                    pm_2_5_value["expected_burn_status"]
                )


    def test_ca_valley_hot_spot_burn_rules(self):
        """California valley hot spot ruleset"""
        from burnday.entities.entity_model import BurnStatus
        from burnday.usecase.zip_code_burn_evaluation_logic import ca_valley_hot_spot_burn_rules


        pm_2_5_values = [
            {"pm_2_5_input": 0.5, "expected_burn_status": "burning discouraged"},
            {"pm_2_5_input": 12.0, "expected_burn_status": "no burning unless registered"},
            {"pm_2_5_input": 20.1, "expected_burn_status": "no burning unless registered"},
            {"pm_2_5_input": 34.9, "expected_burn_status": "no burning unless registered"},
            {"pm_2_5_input": 35.0, "expected_burn_status": "no burning for all"},
            {"pm_2_5_input": 65.2, "expected_burn_status": "no burning for all"},
            {"pm_2_5_input": 79.7, "expected_burn_status": "no burning for all"}
        ]

        for pm_2_5_value in pm_2_5_values:
            with self.subTest(pm_2_5_value=pm_2_5_value):
                burn_status_entity = BurnStatus()
                burn_status_entity.fine_particulate_matter_2_5 = pm_2_5_value["pm_2_5_input"]
                
                ca_valley_hot_spot_burn_rules(populated_burn_status=burn_status_entity)

                self.assertEqual(
                    burn_status_entity.burn_status, 
                    pm_2_5_value["expected_burn_status"]
                )


    def test_ca_south_coast_burn_rules(self):
        """California south coast ruleset"""
        from burnday.entities.entity_model import BurnStatus
        from burnday.usecase.zip_code_burn_evaluation_logic import ca_south_coast_burn_rules


        pm_2_5_values = [
            {"pm_2_5_input": 0.5, "expected_burn_status": "wood burning permitted"},
            {"pm_2_5_input": 12.0, "expected_burn_status": "wood burning permitted"},
            {"pm_2_5_input": 20.1, "expected_burn_status": "wood burning permitted"},
            {"pm_2_5_input": 29.9, "expected_burn_status": "wood burning permitted"},
            {"pm_2_5_input": 30.0, "expected_burn_status": "wood burning prohibited"},
            {"pm_2_5_input": 65.2, "expected_burn_status": "wood burning prohibited"},
            {"pm_2_5_input": 79.7, "expected_burn_status": "wood burning prohibited"}
        ]

        for pm_2_5_value in pm_2_5_values:
            with self.subTest(pm_2_5_value=pm_2_5_value):
                burn_status_entity = BurnStatus()
                burn_status_entity.fine_particulate_matter_2_5 = pm_2_5_value["pm_2_5_input"]
                
                ca_south_coast_burn_rules(populated_burn_status=burn_status_entity)

                self.assertEqual(
                    burn_status_entity.burn_status, 
                    pm_2_5_value["expected_burn_status"]
                )


    def test_washington_state_burn_rules(self):
        """washington state default burn rules"""
        from burnday.entities.entity_model import BurnStatus
        from burnday.entities.domain_specific_terminology import NO_BURN_RESTRICTIONS
        from burnday.usecase.zip_code_burn_evaluation_logic import washington_state_burn_rules


        pm_2_5_values = [
            {"pm_2_5_input": 0.5, "expected_burn_status": NO_BURN_RESTRICTIONS},
            {"pm_2_5_input": 17.0, "expected_burn_status": NO_BURN_RESTRICTIONS},
            {"pm_2_5_input": 29.9, "expected_burn_status": NO_BURN_RESTRICTIONS},
            {"pm_2_5_input": 30.0, "expected_burn_status": NO_BURN_RESTRICTIONS},
            {"pm_2_5_input": 30.1, 
                "expected_burn_status": "stage 1 burn ban is in effect, no wood burning allowed"},
            {"pm_2_5_input": 79.7, 
                "expected_burn_status": "stage 1 burn ban is in effect, no wood burning allowed"}
        ]

        for pm_2_5_value in pm_2_5_values:
            with self.subTest(pm_2_5_value=pm_2_5_value):
                burn_status_entity = BurnStatus()
                burn_status_entity.fine_particulate_matter_2_5 = pm_2_5_value["pm_2_5_input"]
                
                washington_state_burn_rules(populated_burn_status=burn_status_entity)

                self.assertEqual(
                    burn_status_entity.burn_status, 
                    pm_2_5_value["expected_burn_status"]
                )