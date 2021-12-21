from burnday.entities.entity_model import BurnStatus

import logging


def create_burn_status(burn_day, burn_status, county_name):
    """Creates a BurnStatus entity
    
        Parameters
        ----------
        burn_day: datetime.date
            day the burn_status applies to

        burn_status: str
            description of whether fuel burning is allowed for the location

        county_name: str
            name of the county to return burn status of

        Returns
        -------
        burn_status_entity: BurnStatus
            None if any unexpected error occurs

        entity_creation_error: None
            str if any unexpected error occurred
        
    """
    burn_status_entity = BurnStatus()
    entity_creation_error = None
    try:
        burn_status_entity.burn_day = burn_day
        burn_status_entity.burn_status = burn_status
        burn_status_entity.county_name = county_name
        
        logging.info("create_burn_status - BurnStatus entity successfully created")

    except Exception as error_suppression:
        logging.exception("create_burn_status - unable to create entity")
        burn_status_entity = None
        entity_creation_error = str(error_suppression)

    return(burn_status_entity, entity_creation_error)