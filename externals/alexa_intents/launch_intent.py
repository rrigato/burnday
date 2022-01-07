from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type

import logging

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
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
        return is_request_type("LaunchRequest")(handler_input)


    def handle(self, handler_input):
        """Applies business logic for the appropriate class handler

            Parameters
            ----------
            handler_input: ask_sdk_core.handler_input.HandlerInput

            Returns
            -------
            alexa_sdk_response: ask_sdk_model.Response
        """
        skill_startup_message = "Welcome to the burn day tracker"
        logging.info("LaunchRequestHandler - handle")
        return (
            handler_input.response_builder
                .speak(skill_startup_message)
                .ask(skill_startup_message)
                .response
        )
