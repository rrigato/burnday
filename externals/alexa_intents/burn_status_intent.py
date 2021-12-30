from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name

import logging

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
        
        speak_output = "Hello World!"
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

