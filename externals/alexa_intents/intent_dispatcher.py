from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_intent_name
from ask_sdk_core.utils import is_request_type
from ask_sdk_model import Response
from externals.alexa_intents.burn_status_intent import BurnStatusIntentHandler
from externals.alexa_intents.cancel_stop_intent import CancelOrStopIntentHandler
from externals.alexa_intents.help_intent import HelpRequestHandler
from externals.alexa_intents.launch_intent import LaunchRequestHandler
from externals.alexa_exceptions.default_graceful_exit import CatchAllExceptionHandler

import logging


'''
TODO - extract each intent into separate modules
'''


class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logging.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response



def get_alexa_lambda_handler():
    """Retrieves a lambda_handler function after binding all custom skill intent request and
    exception objects

        Returns
        -------
        alexa_lambda_handler: function
            wrapper around a traditional lambda function that takes a lambda_event and lambda_context
            object for an alexa skill
            https://alexa-skills-kit-python-sdk.readthedocs.io/en/latest/api/core.html?highlight=lambda_handler#ask_sdk_core.skill_builder.SkillBuilder.lambda_handler


    """
    logging.info("get_alexa_lambda_handler - SkillBuilder")

    alexa_skill = SkillBuilder()

    '''
        request handlers are processed from top to bottom
    '''
    alexa_skill.add_request_handler(LaunchRequestHandler())
    alexa_skill.add_request_handler(BurnStatusIntentHandler())
    alexa_skill.add_request_handler(HelpRequestHandler())
    alexa_skill.add_request_handler(CancelOrStopIntentHandler())
    alexa_skill.add_request_handler(FallbackIntentHandler())
    alexa_skill.add_request_handler(SessionEndedRequestHandler())

    alexa_skill.add_exception_handler(CatchAllExceptionHandler())

    logging.info("get_alexa_lambda_handler - returning alexa_lambda_handler")
    return(alexa_skill.lambda_handler())