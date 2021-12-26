from burnday.entities.entity_model import BurnStatus

import logging


def create_burn_status(burn_day, air_quality_index, zip_code):
    """Creates a BurnStatus entity
    
        Parameters
        ----------
        burn_day: datetime.date
            day the burn_status applies to

        air_quality_index: int
            Air quality index for the given location

        zip_code: int
            numeric postal code

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
        burn_status_entity.air_quality_index = air_quality_index
        burn_status_entity.zip_code = zip_code
        
        logging.info("create_burn_status - BurnStatus entity successfully created")

    except Exception as error_suppression:
        logging.exception("create_burn_status - unable to create entity")
        burn_status_entity = None
        entity_creation_error = str(error_suppression)

    return(burn_status_entity, entity_creation_error)