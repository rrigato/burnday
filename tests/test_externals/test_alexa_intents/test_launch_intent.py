from copy import deepcopy

import json
import unittest

class TestLaunchIntent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open("tests/events/intent_requests/launch_intent.json", "r") as intent_request:
            cls.intent_request = json.load(intent_request)

    def test_launch_intent(self):
        """LaunchRequest for initally opening the skill"""
        from externals.alexa_intents.intent_dispatcher import get_alexa_lambda_handler

        expected_response_message = "What location would you like the burn status for?"
        alexa_lambda_handler = get_alexa_lambda_handler()

        self.assertTrue(
            expected_response_message in 
            alexa_lambda_handler(
                deepcopy(self.intent_request), 
                None
            )["response"]["outputSpeech"]["ssml"]
        )



