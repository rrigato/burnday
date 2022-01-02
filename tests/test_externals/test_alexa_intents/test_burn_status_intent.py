from copy import deepcopy
from unittest.mock import patch

import json
import unittest

class TestBurnStatusIntent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open("tests/events/intent_requests/burn_status_intent.json", "r") as intent_request:
            cls.intent_request = json.load(intent_request)


    @patch("externals.alexa_intents.burn_status_intent.location_burn_status")
    @patch("externals.alexa_intents.burn_status_intent.validate_location_burn_status")
    def test_burn_status_intent(self, mock_validate_location_burn_status, 
        mock_location_burn_status):
        """BurnStatusIntentHandler.handle executes usecase and returns burn status"""
        from burnday.entities.entity_model import BurnStatus
        from burnday.entry.response_objects import ResponseSuccess
        from externals.alexa_intents.intent_dispatcher import get_alexa_lambda_handler
        
        expected_message = "mock burn status message returned from usecase"
        mock_burn_status_entity = BurnStatus()
        mock_burn_status_entity.burn_status = expected_message
        mock_validate_location_burn_status.return_value = True
        mock_location_burn_status.return_value = ResponseSuccess(
            response_value=mock_burn_status_entity
        )

        alexa_lambda_handler = get_alexa_lambda_handler()


        actual_response_message = alexa_lambda_handler(
            deepcopy(self.intent_request), 
            None
        )


        mock_validate_location_burn_status.assert_called_once_with(
            zip_code=int(
                self.intent_request["request"]["intent"]["slots"]["burn_location"]["value"]
            )
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

        self.assertTrue(actual_response_message["response"]["shouldEndSession"])


    @patch("externals.alexa_intents.burn_status_intent.BurnStatusIntentHandler.handle")
    def test_burn_status_intent_unexpected_error(self, mock_burn_status_handle):
        """BurnStatusIntentHandler.handle raises unexpected errror that is handled gracefully"""
        from externals.alexa_intents.intent_dispatcher import get_alexa_lambda_handler

        alexa_lambda_handler = get_alexa_lambda_handler()

        mock_burn_status_handle.side_effect = TimeoutError("Unexpected Network timeout")

        actual_response_message = alexa_lambda_handler(
            deepcopy(self.intent_request), 
            None
        )

        self.assertEqual(type(actual_response_message["response"]["outputSpeech"]["ssml"]), str)
    
        self.assertTrue(actual_response_message["response"]["shouldEndSession"])



    @patch("externals.alexa_intents.burn_status_intent.location_burn_status")
    @patch("externals.alexa_intents.burn_status_intent.validate_location_burn_status")
    def test_burn_status_intent_response_failure(self, mock_validate_location_burn_status, 
        mock_location_burn_status):
        """location_burn_status usecase returns a ResponseFailure object"""
        from burnday.entry.response_objects import ResponseFailure
        from externals.alexa_intents.intent_dispatcher import get_alexa_lambda_handler
        
        mock_error_message = "_handle_api_request - api_response.getcode - 400"
        expected_message = ("Something went wrong when attempting to retrieve" + 
            " the burn status for that location, please try again later"
        )
        mock_validate_location_burn_status.return_value = True
        mock_location_burn_status.return_value = ResponseFailure(
            error_message=mock_error_message
        )

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
