from burnday.entities.zip_codes import california
from burnday.usecase.air_quality_index_conversions import aqi_to_pm_2point5
from burnday.usecase.zip_code_burn_evaluation_logic import ca_south_coast_burn_rules
from burnday.usecase.zip_code_burn_evaluation_logic import california_valley_default_burn_rules
from burnday.usecase.zip_code_burn_evaluation_logic import ca_valley_hot_spot_burn_rules
from burnday.usecase.zip_code_burn_evaluation_logic import default_burn_rules
from burnday.usecase.zip_code_burn_evaluation_logic import washington_state_burn_rules

import logging


def _zip_based_mapping():
    """Dict that routes to applicable factory function based on zip_code key
    
        Returns
        -------
        dispatch_functions: dict
            Where each key is the int zip_code for the burn status request and 
            each value is the factory function to execute the appropriate business logic
    """
    zip_code_router = {}

    for zip_code in range(0, 100000):
        zip_code_router[zip_code] = default_burn_rules

    return(zip_code_router)
    

def _apply_california_valley_default_burn_rules(dispatch_functions):
    """Zip codes that use the california_valley_default_burn_rules ruleset
    
        Parameters
        -------
        dispatch_functions: dict
            Where each key is the int zip_code for the burn status request and 
            each value is the factory function to execute the appropriate business logic
    """
    ca_valley_default_zip_codes = []
    ca_valley_default_zip_codes.extend(california.tulare_county)

    for ca_default_zip in ca_valley_default_zip_codes:
        dispatch_functions[ca_default_zip] = california_valley_default_burn_rules


def _apply_ca_valley_hot_spot_burn_rules(dispatch_functions):
    """Zip codes that use the ca_valley_hot_spot_burn_rules ruleset
    
        Parameters
        -------
        dispatch_functions: dict
            Where each key is the int zip_code for the burn status request and 
            each value is the factory function to execute the appropriate business logic
    """
    hot_spot_zip_codes = []
    hot_spot_zip_codes.extend(california.kern_county)

    for ca_hot_spot_zip in hot_spot_zip_codes:
        dispatch_functions[ca_hot_spot_zip] = ca_valley_hot_spot_burn_rules


def _apply_ca_south_coast_burn_rules(dispatch_functions):
    """Zip codes that use the ca_south_coast_burn_rules ruleset
    
        Parameters
        -------
        dispatch_functions: dict
            Where each key is the int zip_code for the burn status request and 
            each value is the factory function to execute the appropriate business logic
    """
    hot_spot_zip_codes = []
    hot_spot_zip_codes.extend(california.los_angeles_county)
    hot_spot_zip_codes.extend(california.san_bernardino_county)

    for ca_hot_spot_zip in hot_spot_zip_codes:
        dispatch_functions[ca_hot_spot_zip] = ca_south_coast_burn_rules


def _apply_washington_state_burn_rules(dispatch_functions):
    """All zip codes in the state of Washington use the washington_state_burn_rules ruleset
    
        Parameters
        -------
        dispatch_functions: dict
            Where each key is the int zip_code for the burn status request and 
            each value is the factory function to execute the appropriate business logic
    """
    for wa_state_zip_code in range(98000, 99499 + 1):
        dispatch_functions[wa_state_zip_code] = washington_state_burn_rules
    
    logging.info("_apply_washington_state_burn_rules - complete")



def factory_router(populated_burn_status):
    """Mutates populated_burn_status.burn_status with applicable business logic
    
        Parameters
        ----------
        populated_burn_status: BurnStatus
            if populated_burn_status.air_quality_index is None, 
            no attributes are modified
    """
    aqi_to_pm_2point5(populated_burn_status=populated_burn_status)

    logging.info("factory_router - aqi_to_pm_2point5 complete")

    dispatch_functions = _zip_based_mapping()

    _apply_ca_south_coast_burn_rules(dispatch_functions=dispatch_functions)
    _apply_california_valley_default_burn_rules(dispatch_functions=dispatch_functions)
    _apply_ca_valley_hot_spot_burn_rules(dispatch_functions=dispatch_functions)
    _apply_washington_state_burn_rules(dispatch_functions=dispatch_functions)

    logging.info("factory_router - custom rulesets mapped")

    dispatch_functions[populated_burn_status.zip_code](populated_burn_status=populated_burn_status)
    
    logging.info("factory_router - mapped function invocation complete")
