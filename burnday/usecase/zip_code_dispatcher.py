from copy import deepcopy

from burnday.usecase import zip_code_burn_evaluation_logic

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
    

def factory_router(populated_burn_status):
    """Mutates populated_burn_status.burn_status with applicable business logic
    
        Parameters
        ----------
        populated_burn_status: BurnStatus
            if populated_burn_status.air_quality_index is None, 
            no attributes are modified
    """
    dispatch_functions = _zip_based_mapping()

    dispatch_functions[populated_burn_status.zip_code](populated_burn_status=populated_burn_status)
