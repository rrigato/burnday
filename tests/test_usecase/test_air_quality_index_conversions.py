import unittest

class TestAirQualityIndexConversions(unittest.TestCase):

    def test_aqi_to_pm_2point5(self):
        """BurnStatus.fine_particulate_matter_2_5 attribute updated"""
        from burnday.entities.entity_model import BurnStatus
        from burnday.usecase.air_quality_index_conversions import aqi_to_pm_2point5

        burn_status_entity = BurnStatus()

        aqi_test_values = [
            {"aqi_input": 17, "expected_pm_2_5": 4.080},
            {"aqi_input": 74, "expected_pm_2_5": 23.037},
            {"aqi_input": 123, "expected_pm_2_5": 44.435},
            {"aqi_input": 189, "expected_pm_2_5": 129.096},
            {"aqi_input": 201, "expected_pm_2_5": 150.500},
            {"aqi_input": 349, "expected_pm_2_5": 298.936}
        ]

        for aqi_test_value in aqi_test_values:
            with self.subTest(aqi_test_value=aqi_test_value):
                burn_status_entity.air_quality_index = aqi_test_value["aqi_input"]
                
                aqi_to_pm_2point5(populated_burn_status=burn_status_entity)

                self.assertEqual(
                    burn_status_entity.fine_particulate_matter_2_5, 
                    aqi_test_value["expected_pm_2_5"]
                )


    def test_aqi_to_pm_2point5_air_quality_index_is_none(self):
        """air_quality_index attr is None, no mutation occurred on fine_particulate_matter_2_5"""
        from burnday.entities.entity_model import BurnStatus
        from burnday.usecase.air_quality_index_conversions import aqi_to_pm_2point5
        from datetime import date

        mock_burn_day = "3005-11-29"
        mock_zip_code = 20002
        mock_air_quality_index = None

        burn_status_entity = BurnStatus()

        burn_status_entity.burn_day = date.fromisoformat(mock_burn_day)
        burn_status_entity.zip_code = mock_zip_code
        burn_status_entity.air_quality_index = mock_air_quality_index


        aqi_to_pm_2point5(populated_burn_status=burn_status_entity)


        self.assertEqual(burn_status_entity.burn_day.isoformat(), mock_burn_day)
        self.assertEqual(burn_status_entity.zip_code, mock_zip_code)
        self.assertEqual(burn_status_entity.air_quality_index, mock_air_quality_index)
        self.assertIsNone(burn_status_entity.air_quality_index)
        self.assertIsNone(burn_status_entity.fine_particulate_matter_2_5)


    def test_aqi_to_pm_10(self):
        """BurnStatus.fine_particulate_matter_2_5 attribute updated"""
        pass

    def test_aqi_to_pm_10_air_quality_index_is_none(self):
        """air_quality_index attr is None, no mutation occurred on coarse_particulate_matter_10"""
        pass