from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_intent_name
from ask_sdk_model import Response

import logging

class HelpRequestHandler(AbstractRequestHandler):
    """Handler for when the user asks for help"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        output_message = "Provide a zip code to receive that location's burn status"
        logging.info("HelpRequestHandler - handle")
        return (
            handler_input.response_builder
                .speak(output_message)
                .response
        )
