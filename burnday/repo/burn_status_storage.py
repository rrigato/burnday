from burnday.repo.entity_serialization import create_burn_status

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
    from datetime import date
    return(
        create_burn_status(
            burn_day=date.today(),
            air_quality_index=123,
            zip_code=zip_code
        
        )
    )