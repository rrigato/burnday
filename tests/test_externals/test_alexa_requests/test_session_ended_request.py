import json
import unittest

class TestSessionEndedRequest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open("tests/events/intent_requests/session_ended_request.json", "r") as intent_request:
            cls.intent_request = json.load(intent_request)


    def test_session_ended_request(self):
        """If cleanup logic is ever required, write test case here"""
        from externals.alexa_requests.session_ended_request import SessionEndedRequestHandler