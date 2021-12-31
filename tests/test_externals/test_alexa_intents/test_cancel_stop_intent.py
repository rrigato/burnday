from copy import deepcopy

import json
import unittest

class TestCancelStopIntent(unittest.TestCase):


    def test_cancel_stop_intent(self):
        """StopIntent and CancelIntent handle skill invocation cleanup"""
        from externals.alexa_intents.intent_dispatcher import get_alexa_lambda_handler

        expected_response_message = "later"

        json_intent_events = [
            "tests/events/intent_requests/cancel_intent.json",
            "tests/events/intent_requests/stop_intent.json"
        ]

        for json_intent_event in json_intent_events:
            with self.subTest(json_intent_event=json_intent_event):

                with open(json_intent_event, "r") as intent_request:
                    intent_request = json.load(intent_request)


                alexa_lambda_handler = get_alexa_lambda_handler()


                self.assertTrue(
                    expected_response_message in 
                    alexa_lambda_handler(
                        deepcopy(intent_request), 
                        None
                    )["response"]["outputSpeech"]["ssml"].lower()
                )

