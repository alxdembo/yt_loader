import boto3
from flask import current_app


def get_s3_resource():
    return boto3.resource(
        's3',
        aws_access_key_id=current_app.config['AWS_KEY_ID'],
        aws_secret_access_key=current_app.config['AWS_SECRET'])


def get_s3_client():
    return boto3.client(
        's3',
        aws_access_key_id=current_app.config['AWS_KEY_ID'],
        aws_secret_access_key=current_app.config['AWS_SECRET'])
