from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_intent_name
from ask_sdk_core.utils import is_request_type
from ask_sdk_model import Response

import logging

class DefaultExceptionHandler(AbstractExceptionHandler):
    """Default error message returned to user if an intent is not handled or an intent handler
    throws an unexpected error"""

    def can_handle(self, handler_input, exception):
        """Determines the type of input the class can handle

            Parameters
            ----------
            handler_input: ask_sdk_core.handler_input.HandlerInput

            Returns
            -------
            can_class_handle_request: bool
                True if this class can handle the provided request, False otherwise
        """
        return(True)

    def handle(self, handler_input, exception):
        """Applies business logic for the appropriate class handler

            Parameters
            ----------
            handler_input: ask_sdk_core.handler_input.HandlerInput

            Returns
            -------
            alexa_sdk_response: ask_sdk_model.Response
        """
        logging.error(exception, exc_info=True)

        speak_output = "Unexpected error, looks like you found a bug before the developers did!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(True)
                .response
        )


