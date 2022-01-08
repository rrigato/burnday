from burnday.entry.entry_burn_status import location_burn_status
from burnday.entry.entry_burn_status import validate_location_burn_status
from externals.alexa_intents.intent_dispatcher import get_alexa_lambda_handler

import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)


alexa_lambda_handler = get_alexa_lambda_handler()


if __name__ == "__main__":
    import json
    import os
    os.environ["AWS_REGION"] = "us-east-1"

    with open("tests/events/intent_requests/burn_status_intent.json", "r") as intent_request:
        intent_request = json.load(intent_request)
    print(alexa_lambda_handler(intent_request, None)["response"]["outputSpeech"]["ssml"])