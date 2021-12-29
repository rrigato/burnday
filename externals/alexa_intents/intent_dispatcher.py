from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from externals.alexa_intents.launch_intent import LaunchRequestHandler


def get_alexa_lambda_handler():
    """Retrieves a lambda_handler for different alexa skills kit sdk 

            
        Returns
        -------
        alexa_lambda_handler: function
            wrapper around a traditional lambda function that takes a lambda_event and lambda_context
            object for an alexa skill
            https://alexa-skills-kit-python-sdk.readthedocs.io/en/latest/api/core.html?highlight=lambda_handler#ask_sdk_core.skill_builder.SkillBuilder.lambda_handler


    """
    '''
        TODO - 
        
        
        alexa_skill.add_request_handler(HelloWorldIntentHandler())
        alexa_skill.add_request_handler(HelpIntentHandler())
        alexa_skill.add_request_handler(CancelOrStopIntentHandler())
        alexa_skill.add_request_handler(FallbackIntentHandler())
        alexa_skill.add_request_handler(SessionEndedRequestHandler())

        alexa_skill.add_exception_handler(CatchAllExceptionHandler())

        
    '''
    alexa_skill = SkillBuilder()
    alexa_skill.add_request_handler(LaunchRequestHandler())
    return(alexa_skill.lambda_handler())