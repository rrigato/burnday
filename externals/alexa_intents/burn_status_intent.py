from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_intent_name
from ask_sdk_model import Response

import logging

class BurnStatusIntentHandler(AbstractRequestHandler):
    """Handler for retrieving the Burn Status for a location specified by a user"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("BurnStatusIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

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
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

