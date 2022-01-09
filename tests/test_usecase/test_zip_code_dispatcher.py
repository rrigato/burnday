from unittest.mock import MagicMock
from unittest.mock import patch

import unittest

class TestZipCodeDispatcher(unittest.TestCase):
    def test_zip_based_mapping(self):
        """100000 item dict has one function handling each zip code"""
        from burnday.usecase.zip_code_dispatcher import _zip_based_mapping
        from inspect import isfunction


        dispatch_functions = _zip_based_mapping()


        [
            self.assertTrue(isfunction(dispatch_function)) 
            for dispatch_function in dispatch_functions.values()
        ]
        [self.assertEqual(type(zip_code), int) for zip_code in dispatch_functions.keys()]
        self.assertEqual(len(dispatch_functions.keys()), 100000)



    @patch("burnday.usecase.zip_code_dispatcher.aqi_to_pm_2point5")
    @patch("burnday.usecase.zip_code_dispatcher._zip_based_mapping")
    def test_factory_router(self, mock_zip_based_mapping, mock_aqi_to_pm_2point5):
        """selects key of _zip_based_mapping and invokes corresponding function with entity"""
        from burnday.entities.entity_model import BurnStatus
        from burnday.usecase.zip_code_burn_evaluation_logic import california_valley_default_burn_rules
        from burnday.usecase.zip_code_dispatcher import factory_router


        mock_business_rule_function = MagicMock()
        mock_burn_status = BurnStatus()
        mock_zip_code = 20002
        mock_dispatch_router = {20002: mock_business_rule_function}
        mock_zip_based_mapping.return_value = mock_dispatch_router
        mock_burn_status.zip_code = mock_zip_code


        factory_router(populated_burn_status=mock_burn_status)


        mock_business_rule_function.assert_called_once_with(populated_burn_status=mock_burn_status)
        mock_aqi_to_pm_2point5.assert_called_once_with(populated_burn_status=mock_burn_status)
        '''Testing random rule set'''
        self.assertEqual(mock_dispatch_router[93261], california_valley_default_burn_rules)
        

    @patch("burnday.usecase.zip_code_dispatcher.washington_state_burn_rules")
    @patch("burnday.usecase.zip_code_dispatcher.aqi_to_pm_2point5")
    def test_apply_washington_state_burn_rules(self, mock_aqi_to_pm_2point5,
        mock_washington_state_burn_rules):
        """Washington state zip codes correct callback function"""
        from burnday.entities.entity_model import BurnStatus
        from burnday.usecase.zip_code_dispatcher import factory_router

        wa_boundary_zip_codes = [
            {"zip_code": 97999, "expected_callback_function_call_count": 0},
            {"zip_code": 98000, "expected_callback_function_call_count": 1},
            {"zip_code": 98078, "expected_callback_function_call_count": 1},
            {"zip_code": 99451, "expected_callback_function_call_count": 1},
            {"zip_code": 99499, "expected_callback_function_call_count": 1},
            {"zip_code": 99500, "expected_callback_function_call_count": 0}
        ]

        for wa_boundary_zip_code in wa_boundary_zip_codes:
            with self.subTest(wa_boundary_zip_code=wa_boundary_zip_code):
                mock_burn_status = BurnStatus()
                mock_burn_status.zip_code = wa_boundary_zip_code["zip_code"]
                mock_burn_status.air_quality_index = 123

                factory_router(populated_burn_status=mock_burn_status)


                self.assertEqual(
                    mock_washington_state_burn_rules.call_count,
                    wa_boundary_zip_code["expected_callback_function_call_count"]
                )

                mock_washington_state_burn_rules.reset_mock()


    @patch("burnday.usecase.zip_code_dispatcher.ca_valley_hot_spot_burn_rules")
    @patch("burnday.usecase.zip_code_dispatcher.aqi_to_pm_2point5")
    def test_apply_ca_valley_hot_spot_burn_rules(self, mock_aqi_to_pm_2point5,
        mock_ca_valley_hot_spot_burn_rules):
        """California Valley hot spot rule zip codes correct callback function"""
        from burnday.entities.entity_model import BurnStatus
        from burnday.usecase.zip_code_dispatcher import factory_router

        ca_hot_spot_zips = [
            {"zip_code": 93304, "expected_callback_function_call_count": 1},
            {"zip_code": 93240, "expected_callback_function_call_count": 1},
            {"zip_code": 93313, "expected_callback_function_call_count": 1}
        ]

        for ca_hot_spot_zip in ca_hot_spot_zips:
            with self.subTest(ca_hot_spot_zip=ca_hot_spot_zip):
                mock_burn_status = BurnStatus()
                mock_burn_status.zip_code = ca_hot_spot_zip["zip_code"]
                mock_burn_status.air_quality_index = 123

                factory_router(populated_burn_status=mock_burn_status)


                self.assertEqual(
                    mock_ca_valley_hot_spot_burn_rules.call_count,
                    ca_hot_spot_zip["expected_callback_function_call_count"]
                )

                mock_ca_valley_hot_spot_burn_rules.reset_mock()


    @patch("burnday.usecase.zip_code_dispatcher.ca_south_coast_burn_rules")
    @patch("burnday.usecase.zip_code_dispatcher.aqi_to_pm_2point5")
    def test_apply_ca_south_coast_burn_rules(self, mock_aqi_to_pm_2point5,
        mock_ca_south_coast_burn_rules):
        """ca_south_coast_burn_rules invoked as callback function for sample zip codes"""
        from burnday.entities.entity_model import BurnStatus
        from burnday.usecase.zip_code_dispatcher import factory_router

        ca_south_coast_zips = [
            {"zip_code": 89999, "expected_callback_count": 0, "county": "out of scope zip code"},

            {"zip_code": 90001, "expected_callback_count": 1, "county": "los_angeles"},
            {"zip_code": 90012, "expected_callback_count": 1, "county": "los_angeles"},
            {"zip_code": 90028, "expected_callback_count": 1, "county": "los_angeles"},
            {"zip_code": 90037, "expected_callback_count": 1, "county": "los_angeles"},
            {"zip_code": 93599, "expected_callback_count": 1, "county": "los_angeles"},

            {"zip_code": 91701, "expected_callback_count": 1, "county": "san_bernardino"},
            {"zip_code": 91785, "expected_callback_count": 1, "county": "san_bernardino"},
            {"zip_code": 92286, "expected_callback_count": 1, "county": "san_bernardino"},
            {"zip_code": 92334, "expected_callback_count": 1, "county": "san_bernardino"},
            {"zip_code": 93592, "expected_callback_count": 1, "county": "san_bernardino"},

            {"zip_code": 90620, "expected_callback_count": 1, "county": "orange_county"},
            {"zip_code": 90743, "expected_callback_count": 1, "county": "orange_county"},
            {"zip_code": 92610, "expected_callback_count": 1, "county": "orange_county"},
            {"zip_code": 92821, "expected_callback_count": 1, "county": "orange_county"},
            {"zip_code": 92899, "expected_callback_count": 1, "county": "orange_county"},

            {"zip_code": 93601, "expected_callback_count": 0, "county": "out of scope zip code"}
            
        ]

        for ca_south_coast_zip in ca_south_coast_zips:
            with self.subTest(ca_south_coast_zip=ca_south_coast_zip):
                mock_burn_status = BurnStatus()
                mock_burn_status.zip_code = ca_south_coast_zip["zip_code"]
                mock_burn_status.air_quality_index = 123

                factory_router(populated_burn_status=mock_burn_status)


                self.assertEqual(
                    mock_ca_south_coast_burn_rules.call_count,
                    ca_south_coast_zip["expected_callback_count"],
                    
                    msg="\n**Failing location** \nCounty - {county} \nZip - {zip_code}".format(
                        county=ca_south_coast_zip["county"],
                        zip_code=ca_south_coast_zip["zip_code"]
                    )  
                )

            mock_ca_south_coast_burn_rules.reset_mock()