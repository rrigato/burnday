from copy import deepcopy
from unittest.mock import patch

import json
import unittest

class TestBurnStatusIntent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open("tests/events/intent_requests/burn_status_intent.json", "r") as intent_request:
            cls.intent_request = json.load(intent_request)

    @unittest.skip("Skipping for now")
    def test_burn_status_intent(self):
        """"""
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
                {expected_response} 
                Actual Alexa Response - 
                {actual_response}
            """.format(
                    expected_response=expected_message,
                    actual_response=actual_response_message["response"]["outputSpeech"]["ssml"]
                )
        )


    @patch("externals.alexa_intents.burn_status_intent.BurnStatusIntentHandler.handle")
    def test_burn_status_intent_unexpected_error(self, mock_burn_status_handle):
        """BurnStatusIntentHandler.handle raises unexpected errror"""
        from externals.alexa_intents.intent_dispatcher import get_alexa_lambda_handler

        alexa_lambda_handler = get_alexa_lambda_handler()

        mock_burn_status_handle.side_effect = TimeoutError("Unexpected Network timeout")

        actual_response_message = alexa_lambda_handler(
            deepcopy(self.intent_request), 
            None
        )

        self.assertEqual(type(actual_response_message["response"]["outputSpeech"]["ssml"]), str)