from burnday.repo.entity_serialization import create_burn_status

def burn_status_for_zip(zip_code):
    """Retrieves a BurnStatus entity from persistant storage for a zip_code

        Parameters
        ----------
        zip_code: int
            numeric postal code
            
        Returns
        -------
        zip_burn_status: BurnStatus
            None if no BurnStatus entites were found for the passed zip_code

        repo_retrieval_error: None
            str if any unexpected error occurred when retrieving the BurnStatus entity 
    """
    '''
        TODO - 
        API call to load AQI from persistant storage
        https://docs.airnowapi.org/forecastsbyzip/docs

        check for following boundary condition for AQI
        When a numerical AQI value is not available, 
        such as when only a categorical forecast has been submitted, a -1 will be returned.

        try except for any unexpected exceptions

        return(create_burn_status(), None)

    '''
    pass