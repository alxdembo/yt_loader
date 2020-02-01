from flask import current_app
from utils.s3_base import get_s3_resource, get_s3_client


def get_s3_upload_url(file_name):
    get_s3_resource().Object(
        current_app.config['BUCKET_NAME'],
        f"{current_app.config['TMP_FOLDER']}/sliced_{file_name}").upload_file(Filename="sliced_" + file_name)

    return get_s3_client().generate_presigned_url('get_object',
                                                  Params={'Bucket': current_app.config['BUCKET_NAME'],
                                                          'Key': "sliced_" + file_name},
                                                  ExpiresIn=current_app.config['URL_EXPIRATION_INTERVAL'])
