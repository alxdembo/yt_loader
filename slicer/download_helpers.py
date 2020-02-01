import requests
from flask import current_app


class DownloadHelpers:
    @staticmethod
    def download_youtube(video_id):
        from pytube import YouTube
        video = YouTube(current_app.config['STREAM_HOST_URIS']['youtube'] + video_id, defer_prefetch_init=False)
        video.streams.first().download()

    @staticmethod
    def download_ooyala(video_id):
        r = requests.get(
            f"{current_app.config['STREAM_HOST_URIS']['ooyala'] + video_id}/{current_app.config['OOYALA_TOKEN']}",
            stream=True)
        with open('file.mp4', 'wb') as f:
            for chunk in r.iter_content(256):
                f.write(chunk)
