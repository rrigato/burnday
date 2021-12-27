import boto3
import json
import logging
import os

def get_burnday_secrets():
    """Loads burnday project secrets and configuration from persistant storage

        Returns
        -------
        burnday_project_config: dict
            burnday project secrets and config with the following keys:
            {
                "airnow_api_key": str,
                "aqs_email": str,
                "aqs_key": str
            }
            None if any unexpected errors occur

        repo_retrieval_error: None
            str if any unexpected error occurred when retrieving project secrets and config
    """
    try:
        ssm_client = boto3.client("ssm", region_name=os.environ.get("AWS_REGION"))

        logging.info("get_burnday_secrets - ssm_client created")

        return(
            json.loads(
                ssm_client.get_parameter(
                    Name="/burnday/v1", 
                    WithDecryption=True
                )["Parameter"]["Value"]
            ), 
            None
        )

    except Exception as error_suppression:
        
        logging.exception("get_burnday_secrets - unexpected error")
        return(None, str(error_suppression))


if __name__ == "__main__":
    os.environ["AWS_REGION"] = "us-east-1"
    burnday_project_config, repo_retrieval_error = get_burnday_secrets()
    print(burnday_project_config)