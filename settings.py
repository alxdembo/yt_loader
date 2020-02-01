BUCKET_NAME = 'dembo-test-task'
URL_EXPIRATION_INTERVAL = 3600

TMP_FOLDER = 'tmp'
AWS_REGION = 'eu-west-2'

STREAM_HOST_URIS = {
    'youtube': 'https://www.youtube.com/watch?v=',
    'ooyala': 'http://85072-c.ooyala.com/'
}

YOUTUBE_URI = 'https://www.youtube.com/watch?v='
OOYALA_URI = 'http://85072-c.ooyala.com/'

try:
    from .settings_local import *
except ImportError:
    pass
