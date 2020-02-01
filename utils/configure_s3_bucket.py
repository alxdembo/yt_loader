from math import ceil
from botocore.exceptions import ClientError
from settings import BUCKET_NAME, URL_EXPIRATION_INTERVAL
from utils.s3_base import get_s3_client


def configure_bucket(bucket_name, object_expiration):
    # amazon checks lifecycle daily
    days = ceil(object_expiration / (24 * 3600))

    try:
        get_s3_client().put_bucket_lifecycle_configuration(
            Bucket=bucket_name,
            LifecycleConfiguration={
                "Rules": [
                    {
                        "Expiration": {"Days": days},
                        "ID": "wholebucket",
                        "Filter": {},
                        "Status": "Enabled",
                    }
                ]
            })
    except ClientError as e:
        print(f"Unable to apply bucket policy. \nReason:{e}")


if __name__ == '__main__':
    configure_bucket(BUCKET_NAME, URL_EXPIRATION_INTERVAL)
