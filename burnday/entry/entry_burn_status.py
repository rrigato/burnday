from burnday.entry.input_valdiators import validate_str_input
from burnday.entry.request_objects import InvalidRequest
from burnday.entry.request_objects import ValidRequest

import logging


def county_burn_status(county_burn_status_request):
    """Get the daily burn status for every county

        Parameters
        ----------
        county_burn_status_request: ValidRequest
            county_burn_status_request.request_filters:
            {
                "county_name": str
            }

        Returns
        -------
        county_burn_status_response: ResponseSuccess or ResponseFailure
            county_burn_status_response.response_value is a list of dict where each dict has the keys:
            {
                "burn_day": datetime.date,
                "burn_status": str,
                "county_name": str
            }
            if no burn status results are found for the given county_name,
            county_burn_status_response.response_value=None

            county_burn_status_response will be a ResponseFailure if any unexpected errors 
            occur when processing the usecase
    """
    '''
        TODO -
        county_burn_status, burn_status_error = repo.burn_status_storage.burn_status_for_county
        return ResponseSuccess(response_value=county_burn_status)
        or ResponseFailure
    '''
    pass


def validate_county_burn_status(county_name):
    """Get a valid request for calling county_burn_status

        Parameters
        ----------
        county_name: str
            name of the county to return burn status of

        Returns
        -------
        county_burn_status_request: ValidRequest or InvalidRequest
            request_filters attribute:
            {
                "county_name": str
            }
            InvalidRequest is returned if the input does not pass validation
            
    """
    county_name_validation = validate_str_input(str_input=county_name, max_len=150)

    if county_name_validation is not None:
        logging.info("validate_county_burn_status - county_name did not pass input validation")
        return(InvalidRequest(error_message=county_name_validation))

    logging.info("validate_county_burn_status - returning a ValidRequest")
    return(ValidRequest(request_filters={"county_name": county_name}))