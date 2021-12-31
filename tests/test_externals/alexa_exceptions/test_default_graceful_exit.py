from copy import deepcopy
from unittest.mock import patch

import json
import unittest

class TestDefaultGracefulExitIntent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open("tests/events/intent_requests/burn_status_intent.json", "r") as intent_request:
            cls.intent_request = json.load(intent_request)


    @patch("externals.alexa_intents.burn_status_intent.BurnStatusIntentHandler.handle")
    def test_blanket_exception_suppression(self, mock_burn_status_handle):
        """CatchAllExceptionHandler.handle no intent handler found for custom skill"""
        from externals.alexa_intents.intent_dispatcher import get_alexa_lambda_handler

        expected_message = (
            "Unexpected error, looks like you found a bug before the developers did!"
        )
        alexa_lambda_handler = get_alexa_lambda_handler()
    
        fake_intent_request = deepcopy(self.intent_request)

        fake_intent_request["request"]["intent"]["name"] = "NotARealIntent"

        actual_response_message = alexa_lambda_handler(
            deepcopy(fake_intent_request), 
            None
        )

        self.assertTrue(
            expected_message in actual_response_message["response"]["outputSpeech"]["ssml"],
            msg="""
                Expected Alexa Response - 
                {expected_response}
                Actual Alexa Response - 
                {actual_response}
            """.format(
                    expected_response=expected_message,
                    actual_response=actual_response_message["response"]["outputSpeech"]["ssml"]
                )
        )