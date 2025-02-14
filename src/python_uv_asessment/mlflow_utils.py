import os

import boto3
import mlflow
from loguru import logger

SERVER_URIS = {
    "sagemaker": "arn:aws:sagemaker:us-east-1:879381254630:mlflow-tracking-server/ml-rd-mlflow-server",
    "local": "http://localhost:5000",
}


def set_mlflow_server(mode: str = "sagemaker"):
    """Points to the desired MLflow Tracking Server.

    Args:
        mode (str, optional): Whether to log to the Sagemaker MLflow Tracking Server
            (`sagemaker` mode) or to a local MLflow Server (`local` mode). Defaults
            to "sagemaker".
    """

    server_uri = SERVER_URIS[mode]
    mlflow.set_tracking_uri(server_uri)

    logger.info(f"MLflow Tracking Server set to {mode} at {server_uri}")


def authenticate_in_aws_sagemaker():
    """
    Authenticates you in AWS Sagemaker. Required to access the Sagemaker MLflow
    Tracking Server from local.
    """

    logger.info("Authenticating to AWS Sagemaker...")

    ml_sagemaker_session = boto3.Session(profile_name="sagemaker")

    credentials = ml_sagemaker_session.get_credentials().get_frozen_credentials()
    os.environ["AWS_ACCESS_KEY_ID"] = credentials.access_key
    os.environ["AWS_SECRET_ACCESS_KEY"] = credentials.secret_key
    os.environ["AWS_SESSION_TOKEN"] = credentials.token

    logger.info("Authentication to AWS Sagemaker successfully done!")
