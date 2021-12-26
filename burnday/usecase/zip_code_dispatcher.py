from burnday.usecase import zip_code_burn_evaluation_logic
from burnday.usecase.air_quality_index_conversions import aqi_to_pm_2point5

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
        zip_code_router[zip_code] = zip_code_burn_evaluation_logic.default_burn_rules

    return(zip_code_router)
    

def _apply_california_valley_default_burn_rules(dispatch_functions):
    """Zip codes that use the california_valley_default_burn_rules ruleset
    
        Parameters
        -------
        dispatch_functions: dict
            Where each key is the int zip_code for the burn status request and 
            each value is the factory function to execute the appropriate business logic
    """
    '''
        TODO - extract into seperate module if zip codes are still used?
    '''
    tulare_county= [
        93201,
        93603,
        93208,
        93615,
        93618,
        93218,
        93219,
        93221,
        93223,
        93235,
        93633,
        93244,
        93247,
        93647,
        93207,
        93256,
        93258,
        93257,
        93260,
        93261,
        93262,
        93265,
        93267,
        93666,
        93270,
        93271,
        93272,
        93673,
        93274,
        93277,
        93291,
        93292,
        93286
    ]
    for tulare_zip_code in tulare_county:
        dispatch_functions[tulare_zip_code] = zip_code_burn_evaluation_logic.california_valley_default_burn_rules


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

    _apply_california_valley_default_burn_rules(dispatch_functions=dispatch_functions)
    '''
        mapping zip codes for this ruleset:
            california_valley_hot_spot_burn_rules
    '''
    logging.info("factory_router - custom rulesets mapped")

    dispatch_functions[populated_burn_status.zip_code](populated_burn_status=populated_burn_status)
    logging.info("factory_router - mapped function invocation complete")
