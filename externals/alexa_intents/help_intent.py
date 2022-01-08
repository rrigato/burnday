from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name

import logging

class HelpRequestHandler(AbstractRequestHandler):
    """Handler for when the user asks for help"""
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

        return(is_intent_name("AMAZON.HelpIntent")(handler_input))

    def handle(self, handler_input):
        """Applies business logic for the appropriate class handler

            Parameters
            ----------
            handler_input: ask_sdk_core.handler_input.HandlerInput

            Returns
            -------
            alexa_sdk_response: ask_sdk_model.Response
        """
        output_message = "Provide a zip code to receive that location's burn status"
        logging.info("HelpRequestHandler - handle")
        return(
            handler_input.response_builder
                .speak(output_message)
                .ask(output_message)
                .response
        )
