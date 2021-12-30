from copy import deepcopy

import json
import unittest

class TestHelpIntent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open("tests/events/intent_requests/help_intent.json", "r") as intent_request:
            cls.intent_request = json.load(intent_request)

    def test_help_intent(self):
        """IntentRequest of type AMAZON.HelpIntent contains expected response"""
        from externals.alexa_intents.intent_dispatcher import get_alexa_lambda_handler

        expected_message = "Provide a zip code to receive that location's burn status"


        alexa_lambda_handler = get_alexa_lambda_handler()


        actual_response_message = alexa_lambda_handler(
            deepcopy(self.intent_request), 
            None
        )

        self.assertTrue(
            expected_message in actual_response_message["response"]["outputSpeech"]["ssml"],
            msg="""
                Expected Alexa Response - 
                '{expected_response}' 
                Actual Alexa Response - 
                {actual_response}
            """.format(
                    expected_response=expected_message,
                    actual_response=actual_response_message
                )
        )

