import boto3
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

        repo_retrieval_error: None
            str if any unexpected error occurred when retrieving the api key
    """
    ssm_client = boto3.client("ssm", region_name=os.environ.get("AWS_REGION"))

    return({}, None)


if __name__ == "__main__":
    os.environ["AWS_REGION"] = "us-east-1"
    get_burnday_secrets()