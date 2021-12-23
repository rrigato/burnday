import unittest

class TestAirQualityIndexMapper(unittest.TestCase):

    def test_aqi_to_pm_breakpoints(self):
        """Ensures air quality index breakpoints are present up through an AQI of 500"""
        from burnday.entities.air_quality_index_mapper import aqi_to_pm_breakpoints

        aqi_breakpoints = aqi_to_pm_breakpoints()

        for possible_aqi_value in range(101):
            with self.subTest(possible_aqi_value=possible_aqi_value):

                self.assertEqual(
                    type(aqi_breakpoints[possible_aqi_value]["aqi_category"]),
                    str
                )

                self.assertEqual(
                    type(aqi_breakpoints[possible_aqi_value]["aqi_lower"]),
                    int
                )

                self.assertEqual(
                    type(aqi_breakpoints[possible_aqi_value]["aqi_upper"]),
                    int
                )

                self.assertEqual(
                    type(aqi_breakpoints[possible_aqi_value]["pm_2_5_lower"]),
                    float
                )

                self.assertEqual(
                    type(aqi_breakpoints[possible_aqi_value]["pm_2_5_upper"]),
                    float
                )

                self.assertEqual(
                    type(aqi_breakpoints[possible_aqi_value]["pm_10_lower"]),
                    float
                )

                self.assertEqual(
                    type(aqi_breakpoints[possible_aqi_value]["pm_10_upper"]),
                    float
                )


                

