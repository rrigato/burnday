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


    '''
        TODO - 
        patch _apply_california_valley_default_burn_rules or
        test output dict directly?
    '''
    @patch("burnday.usecase.zip_code_dispatcher._zip_based_mapping")
    def test_factory_router(self, mock_zip_based_mapping):
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
        '''
            TODO - 
            as-is = test random zip code has the appropriate handler
            patch _apply_california_valley_default_burn_rules or
            test output dict directly?
        '''
        self.assertEqual(mock_dispatch_router[93261], california_valley_default_burn_rules)
