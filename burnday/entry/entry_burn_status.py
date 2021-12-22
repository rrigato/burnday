from burnday.entry.input_valdiators import validate_numeric_input
from burnday.entry.request_objects import InvalidRequest
from burnday.entry.request_objects import ValidRequest

import logging


def location_burn_status(zip_code_burn_status):
    """Get the daily burn status for the requested location

        Parameters
        ----------
        zip_code_burn_status: ValidRequest
            zip_code_burn_status.request_filters:
            {
                "zip_code": int
            }

        Returns
        -------
        location_burn_status_response: ResponseSuccess or ResponseFailure
            location_burn_status_response.response_value is a list of dict where each dict has keys:
            {
                "burn_day": datetime.date,
                "burn_status": str,
                "zip_code": int
            }
            if no burn status results are found for the given zip_code,
            location_burn_status_response.response_value=None

            location_burn_status_response will be a ResponseFailure if any unexpected errors 
            occur when processing the usecase
    """
    '''
        TODO -
        location_burn_status, burn_status_error = repo.burn_status_storage.burn_status_for_zip
        return ResponseSuccess(response_value=location_burn_status)
        or ResponseFailure
    '''
    pass


def validate_location_burn_status(zip_code):
    """Get a valid request for calling location_burn_status

        Parameters
        ----------
        zip_code: int
            numeric postal code

        Returns
        -------
        zip_code_burn_status: ValidRequest or InvalidRequest
            request_filters attribute:
            {
                "zip_code": int
            }
            InvalidRequest is returned if the input does not pass validation
            
    """
    zip_code_validation = validate_numeric_input(
        numeric_input=zip_code, 
        min_val=0,
        max_val=99999
    )


    if zip_code_validation is not None:
        logging.info("validate_location_burn_status - zip_code did not pass input validation")
        return(InvalidRequest(error_message=zip_code_validation))

    logging.info("validate_location_burn_status - returning a ValidRequest")
    return(ValidRequest(request_filters={"zip_code": zip_code}))
