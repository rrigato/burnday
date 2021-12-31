from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name
from burnday.entry.entry_burn_status import location_burn_status
from burnday.entry.entry_burn_status import validate_location_burn_status

import logging

def _orchestrate_usecase():
    """orchestration required to invoke the location_burn_status usecase

        Parameters
        ----------
        handler_input: ask_sdk_core.handler_input.HandlerInput

        Returns
        -------
        burn_status_message: str
            The burn status message or any unexpected errors
    """
    zip_code_request = validate_location_burn_status(zip_code=93261)

    if bool(zip_code_request) == False:
        logging.info("_orchestrate_usecase - invalid zip_code_request")
        return(zip_code_request.error_message)

    logging.info("_orchestrate_usecase - obtained a valid request")

    location_burn_status_response = location_burn_status(zip_code_request=zip_code_request)

    logging.info("_orchestrate_usecase - location_burn_status_response {burn_status}".format(
        burn_status=location_burn_status_response.response_value.burn_status
    ))

    return(location_burn_status_response.response_value.burn_status)

class BurnStatusIntentHandler(AbstractRequestHandler):
    """Handler for retrieving the Burn Status for a location specified by a user"""

    def can_handle(self, handler_input):
        """Determines the type of input the class can handle

            Parameters
            ----------
            handler_input: ask_sdk_core.handler_input.HandlerInput

            Returns
            -------
            can_class_handle_request: bool
                True if this class can handle the provided request, False otherwise
        """
        '''TODO - apply docstr to all handlers
        '''
        return(is_intent_name("BurnStatusIntent")(handler_input))

    def handle(self, handler_input):
        """Applies business logic for the appropriate class handler

            Parameters
            ----------
            handler_input: ask_sdk_core.handler_input.HandlerInput

            Returns
            -------
            alexa_sdk_response: ask_sdk_model.Response
        """
        '''TODO - apply docstr to all handlers
        '''
        logging.info("BurnStatusIntentHandler.handle - ")
        
        speak_output = _orchestrate_usecase()
        '''
            TODO -
            load burn_location slot
            zip_code_request = validate_location_burn_status(zip_code=burn_location_slot)

            location_burn_status_response = location_burn_status(zip_code_request=zip_code_request)

            handler_input.response_builder
                .speak(location_burn_status_response.response_value.burn_status)
                .response
        '''
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

