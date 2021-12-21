def burn_status_for_county(county_name):
    """Retrieves all BurnStatus entities from persistant storage for county_name

        Parameters
        ----------
        county_name: str
            name of the county to return burn status of

        Returns
        -------
        county_burn_status: list
            list of BurnStatus entities or None if no BurnStatus entites were found
            for the passed county_name

        str_validation_error: None
            str if any unexpected error occurred when loading 
    """
    pass