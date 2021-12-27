from burnday.entry.entry_burn_status import location_burn_status
from burnday.entry.entry_burn_status import validate_location_burn_status

import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.basicConfig(format="%(asctime)s %(message)s")

def lambda_handler(event, context):
    zip_code_request = validate_location_burn_status(zip_code=93261)

    location_burn_status_response = location_burn_status(zip_code_request=zip_code_request)

    print(location_burn_status_response.response_value.burn_status)


if __name__ == "__main__":
    import os
    os.environ["AWS_REGION"] = "us-east-1"
    zip_code_request = validate_location_burn_status(zip_code=93261)

    location_burn_status_response = location_burn_status(zip_code_request=zip_code_request)

    logging.info(location_burn_status_response.response_value.burn_status)