from burnday.repo.entity_serialization import create_burn_status
from burnday.repo.persistant_storage import get_burnday_secrets
from datetime import date

import logging


def load_burn_status(zip_code):
    """Retrieves a BurnStatus entity from persistant storage 

        Parameters
        ----------
        zip_code: int
            numeric postal code
            
        Returns
        -------
        burn_status_entity: BurnStatus
            None if no BurnStatus entites were found for the passed zip_code
            Populates the following attributes: 
                burn_status_entity.burn_day = datetime.date
                burn_status_entity.air_quality_index = int
                burn_status_entity.zip_code = zip_code


        repo_retrieval_error: None
            str if any unexpected error occurred when retrieving the BurnStatus entity 
    """
    '''
        TODO - 
        load api credentials
        before making api call:
        str(zip_code).rjust(5, '0')
        API call to load AQI from persistant storage
        https://docs.airnowapi.org/forecastsbyzip/docs

        check for following boundary condition for AQI
        When a numerical AQI value is not available, 
        such as when only a categorical forecast has been submitted, a -1 will be returned.

        try except for any unexpected exceptions

        return(create_burn_status(), None)

    '''
    burnday_project_config, config_retrieval_error = get_burnday_secrets()
    if config_retrieval_error is not None:
        logging.info("load_burn_status - config_retrieval_error")

        return(None, config_retrieval_error)

    return(
        create_burn_status(
            burn_day=date.today(),
            air_quality_index=123,
            zip_code=zip_code
        
        )
    )