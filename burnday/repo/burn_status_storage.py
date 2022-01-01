from burnday.repo.entity_serialization import create_burn_status
from burnday.repo.persistant_storage import get_burnday_secrets
from datetime import date
from urllib.parse import urlencode
from urllib.request import Request
from urllib.request import urlopen

import json
import logging
import uuid

def _get_encoded_parameters(airnow_api_key, zip_code):
    """Returns url encoded query parameters

        Parameters
        ----------
        airnow_api_key: str
            airnow api key for HTTP get request

        zip_code: int
            numeric postal code
            
        Returns
        -------
        url_encoded_query_string: str

    """
    return(urlencode(
        {
            "api_key": airnow_api_key,
            "distance": 500,
            "format": "json",
            "zipCode": str(zip_code).rjust(5, '0')
        }
    ))

def _handle_api_request(airnow_api_key, zip_code):
    """orchestrates api request to AirNow api

        Parameters
        ----------
        airnow_api_key: str
            airnow api key for HTTP get request

        zip_code: int
            numeric postal code
            
        Returns
        -------
        airnow_api_response: list
            list of dict where each dict has the following keys
            {
                "DateIssue": str in YYYY-MM-DD,
                "DateForecast": str in YYYY-MM-DD,
                "ReportingArea": str,
                "StateCode": str ,
                "Latitude": float,
                "Longitude": float,
                "ParameterName": str,
                "AQI": int,
                "Category": {
                    "Number": int,
                    "Name": str
                },
                "ActionDay": boolean,
                "Discussion": str
            } 
            or None if unexpected error occured


        repo_retrieval_error: None
            str if any unexpected error occurred when retrieving the BurnStatus entity 

    """
    try:
        full_request_url = "https://www.airnowapi.org/aq/forecast/zipCode?{query_string}".format(
            query_string=_get_encoded_parameters(airnow_api_key=airnow_api_key, zip_code=zip_code)
        )

        request_id_header = uuid.uuid4().hex

        logging.info("_handle_api_request - request_id_header - " + request_id_header)

        get_request = Request(full_request_url)

        get_request.add_header("x-request-id", request_id_header)

        with urlopen(get_request) as api_response:
            assert api_response.getcode() == 200, (
                "_handle_api_request - api_response.getcode" + str(api_response.getcode())
            )

            return(json.loads(api_response.read()), None)

    except Exception as error_suppression:
        logging.exception("_handle_api_request - unexpected error")
        return(None, str(error_suppression))
    
def _filter_most_recent_forecast(airnow_api_response_dict):
    """Mutates airnow_api_response down to only one element with a DateForecast of 
        datetime.date.today()

        Parameters
        ----------
        airnow_api_response: list
            list of dict where each dict has the following keys
            {
                "DateIssue": str in YYYY-MM-DD,
                "DateForecast": str in YYYY-MM-DD,
                "ReportingArea": str,
                "StateCode": str ,
                "Latitude": float,
                "Longitude": float,
                "ParameterName": str,
                "AQI": int,
                "Category": {
                    "Number": int,
                    "Name": str
                },
                "ActionDay": boolean,
                "Discussion": str
            } 
            or None if unexpected error occured
            
    """
    return(
        airnow_api_response_dict["DateForecast"].strip() == date.today().isoformat()
    )

def _select_todays_air_quality(airnow_api_response, zip_code):
    """selects todays air quality index and creates a BurnStatus entity

        Parameters
        ----------
        airnow_api_response: list
            list of dict where each dict has the following keys
            {
                "DateIssue": str in YYYY-MM-DD,
                "DateForecast": str in YYYY-MM-DD,
                "ReportingArea": str,
                "StateCode": str ,
                "Latitude": float,
                "Longitude": float,
                "ParameterName": str,
                "AQI": int,
                "Category": {
                    "Number": int,
                    "Name": str
                },
                "ActionDay": boolean,
                "Discussion": str
            } 
            or None if unexpected error occured

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
    try:
        if len(airnow_api_response) == 0:
            logging.warning("_select_todays_air_quality - no results returned in list")
            return(None, "No air quality index found for today")

        if len(airnow_api_response) > 1:
            logging.info("_select_todays_air_quality - applying _filter_most_recent_forecast")
            airnow_api_response = list(filter(_filter_most_recent_forecast, airnow_api_response))

        logging.info("_select_todays_air_quality - invoking create_burn_status")
        return(        
            create_burn_status(
                burn_day=date.today(),
                air_quality_index=airnow_api_response[0]["AQI"],
                zip_code=zip_code
            
            )
        )

    except Exception as error_suppression:
        logging.exception("_select_todays_air_quality - unexpected error")
        return(None, str(error_suppression))


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

    airnow_api_response, repo_retrieval_error = _handle_api_request(
        airnow_api_key=burnday_project_config["airnow_key"], 
        zip_code=zip_code
    )

    if repo_retrieval_error is not None:
        logging.info("load_burn_status - _handle_api_request error")
        return(None, repo_retrieval_error)


    logging.info("load_burn_status - _handle_api_request success")
 
    return(
        _select_todays_air_quality(airnow_api_response=airnow_api_response, zip_code=zip_code)
    )


if __name__ == "__main__":
    print(load_burn_status(20002))