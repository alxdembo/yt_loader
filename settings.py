BUCKET_NAME = 'dembo-test-task'
URL_EXPIRATION_INTERVAL = 3600

TMP_FOLDER = 'tmp'
AWS_REGION = 'eu-west-2'

try:
    from .settings_local import *
except ImportError:
    pass
